package main

import (
	"fmt"
	"sync"
)

type Fetcher interface {
	// Fetch returns the body of URL and
	// a slice of URLs found on that page.
	Fetch(url string) (body string, urls []string, err error)
}

type SafeMap struct {
	mu sync.Mutex
	m  map[string]bool
}

// SetAndCheck atomically checks if URL was fetched and marks it as fetched
// Returns true if URL was already fetched, false if it's new
func (c *SafeMap) SetAndCheck(url string) bool {
	c.mu.Lock()
	defer c.mu.Unlock()
	if c.m[url] {
		return true // Already fetched
	}
	c.m[url] = true
	return false // New URL, now marked as fetched
}

// Crawl uses fetcher to recursively crawl
// pages starting with url, to a maximum of depth.
func Crawl(url string, depth int, fetcher Fetcher) {
	cache := &SafeMap{m: make(map[string]bool)}
	var wg sync.WaitGroup
	
	var crawlWorker func(string, int)
	crawlWorker = func(url string, depth int) {
		defer wg.Done()
		
		if depth <= 0 {
			return
		}
		
		// Atomically check and mark URL as fetched
		if cache.SetAndCheck(url) {
			return // Already fetched
		}
		
		body, urls, err := fetcher.Fetch(url)
		if err != nil {
			fmt.Println(err)
			return
		}
		fmt.Printf("found: %s %q\n", url, body)
		
		// Launch goroutines for child URLs
		for _, u := range urls {
			wg.Add(1)
			go crawlWorker(u, depth-1)
		}
	}
	
	wg.Add(1)
	go crawlWorker(url, depth)
	wg.Wait() // Wait for all goroutines to complete
}

func main() {
	Crawl("https://golang.org/", 4, fetcher)
}

// fakeFetcher is Fetcher that returns canned results.
type fakeFetcher map[string]*fakeResult

type fakeResult struct {
	body string
	urls []string
}

func (f fakeFetcher) Fetch(url string) (string, []string, error) {
	if res, ok := f[url]; ok {
		return res.body, res.urls, nil
	}
	return "", nil, fmt.Errorf("not found: %s", url)
}

// fetcher is a populated fakeFetcher.
var fetcher = fakeFetcher{
	"https://golang.org/": &fakeResult{
		"The Go Programming Language",
		[]string{
			"https://golang.org/pkg/",
			"https://golang.org/cmd/",
		},
	},
	"https://golang.org/pkg/": &fakeResult{
		"Packages",
		[]string{
			"https://golang.org/",
			"https://golang.org/cmd/",
			"https://golang.org/pkg/fmt/",
			"https://golang.org/pkg/os/",
		},
	},
	"https://golang.org/pkg/fmt/": &fakeResult{
		"Package fmt",
		[]string{
			"https://golang.org/",
			"https://golang.org/pkg/",
		},
	},
	"https://golang.org/pkg/os/": &fakeResult{
		"Package os",
		[]string{
			"https://golang.org/",
			"https://golang.org/pkg/",
		},
	},
}
