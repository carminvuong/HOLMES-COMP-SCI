; Carmin Vuong <mvuong40@stuy.edu>
; hw 41
; worked with no one, advised by no one

; procedure should produce strings that displays all the movements
(define moveDisksFromSourceToTarget  ; moves disks from the source to the target
  (lambda ( startingCity endingCity storageCity numberofDisksToBeMoved)
    ; numberOfDisksToBeMoved disks moved FROM startingCity TO endingCity, USING storageCity 
    (display "I will move the top ") (display numberofDisksToBeMoved)
    (display " disks from ") (display startingCity) (display " to ")
    (display endingCity)(display " using ") (display storageCity)
    (display " if the Manual says to.")
    (display "\n")
      
    "stub"
  )
)


; test invocations (base cases)
; output: Move top disk from Hanoi to HCMC
(display (moveDisksFromSourceToTarget "Hanoi" "HCMC" "Da Nang" 1))
(display "\n")


; test invocations (recursive cases)
; output: Move top disk from Los Angeles to Paris
;         Move top disk from Los Angeles to Beijing
;         Move top disk from Paris to Beijing
(display (moveDisksFromSourceToTarget "Los Angeles" "Beijing" "Paris" 2))
(display "\n")

