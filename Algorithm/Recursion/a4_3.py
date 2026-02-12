import check

def print_theatre(cinema):
    n = len(cinema)
    def print_seats(row_idx, seat_idx):
        if not cinema[row_idx][1]:
            print()
            return
        is_occupied_str = "X" if cinema[row_idx][1][seat_idx] else "_"
        if seat_idx == len(cinema[row_idx][1]) - 1:
            print("[" + is_occupied_str + "]")
        else:
            print("[" + is_occupied_str + "]", end=" ")
            print_seats(row_idx, seat_idx + 1)
    
    def print_row(row_idx):
        if row_idx == n:
            return
        print("Row " + cinema[row_idx][0] + ":", end=" ")
        print_seats(row_idx, 0)
        
        print_row(row_idx + 1)
        
    print_row(0)
    
def process_bookings(cinema, reqs):
    cinema_labels = list(map(lambda row: row[0], cinema))
    def handle_req(req_idx):
        if req_idx == len(reqs):
            return 0
        
        req_row_label = reqs[req_idx][0]
        # print(req_row_label)
        req_seat_idx = int(reqs[req_idx][1:]) - 1
        # print(req_seat_idx)
        
        if req_row_label not in cinema_labels:
            return 1 + handle_req(req_idx + 1)
        
        req_idx_cinema_label = cinema_labels.index(req_row_label)
        # print(req_idx_cinema_label)
        
        if (not cinema[req_idx_cinema_label][1] or req_seat_idx < 0 or 
        req_seat_idx >= len(cinema[req_idx_cinema_label][1]) or cinema[req_idx_cinema_label][1][req_seat_idx]):
            return 1 + handle_req(req_idx + 1)
        
        cinema[req_idx_cinema_label][1][req_seat_idx] = True
        return 0 + handle_req(req_idx + 1)
    
    count_rej = handle_req(0)
    print_theatre(cinema)
    return count_rej


test_theatre_1 = [
                 ['A', [False, False, False]], 
                 ['B', [False, True, True, False, False]],
                 ['C', [True, False ,False, True, True]],
                 ['D', []],
                 ['E', [False]]
                ]

requests_1 = ['A1', 'C5','B6','E1', 'A1','G3']

expected_theatre_1 = [
    ['A', [True, False, False]],               
    ['B', [False, True, True, False, False]],  
    ['C', [True, False, False, True, True]],   
    ['D', []],                                 
    ['E', [True]]                              
]

EX1_ROW_A = "Row A: [X] [_] [_]"
EX1_ROW_B = "Row B: [_] [X] [X] [_] [_]"
EX1_ROW_C = "Row C: [X] [_] [_] [X] [X]"
EX1_ROW_D = "Row D: "
EX1_ROW_E = "Row E: [X]"
check.set_print_exact(EX1_ROW_A, EX1_ROW_B, EX1_ROW_C, EX1_ROW_D, EX1_ROW_E)

check.expect("Basic Test", 
             process_bookings(test_theatre_1, requests_1), 4)

check.expect("Basic Mutation Test", test_theatre_1, expected_theatre_1)
