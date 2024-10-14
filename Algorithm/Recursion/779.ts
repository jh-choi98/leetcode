function kthGrammar(n: number, k: number): number {
  if (n === 1) {
    return 0;
  } else if (k > 2 ** (n - 2)) {
    return 1 - kthGrammar(n - 1, k - 2 ** (n - 2));
  } else {
    return kthGrammar(n - 1, k);
  }
}
