; Carmin Vuong <mvuong40@stuy.edu>
; hw 40
; worked with no one, advised by no one

; procedure should produce the number of movements required
(define moveDisksFromStartToEnd  ; moves disks from starting point to ending point
  (lambda ( startingCity endingCity storageCity numberofDisksToBeMoved)
    ; numberOfDisksToBeMoved disks moved FROM startingCity TO endingCity, USING storageCity 
   "stubby"
  )
)


; test invocations
(display (moveDisksFromStartToEnd "Hanoi" "HCMC" "Da Nang"2))
(display "\n")

(display (moveDisksFromStartToEnd "HCMC" "Da Nang" "Hanoi" 4))
(display "\n")

(display (moveDisksFromStartToEnd "Da Nang" "Hanoi" "HCMC" 1))
(display "\n")