; Announce what will happen,
; corresponding to the Manual's instruction to
; "Tell us what was requested of you"
(define announce
  (lambda (nDisks source target spare)
    (display "I will move the top ")
    (display nDisks)
    (display " disks \nfrom ")
    (display source)
    (display "\nto ")
    (display target)
    (display "\nusing ")
    (display spare)
    (display " if the Manual says to.\n\n")
  ))

(define separator "\n-----------------\n\n")

; Calculate the instructions for Michael The Bot to
; move "nDisks" from "source" to "target" using "spare".
; Corresponds to the Manual for a Monastery.
(define instructionsForBot
  (lambda (nDisks source target spare)
    (announce nDisks source target spare)
    (if (= nDisks 1)
        (string-append "Move the top disk from " source
                       " to " target ".\n"
                       )
        (string-append (instructionsForBot (- nDisks 1) source spare target)
                       (instructionsForBot 1 source target spare)
                       (instructionsForBot (- nDisks 1) spare target source)
                )
        ) ; end of IF
  ))

; test 0: base case
(define steps (instructionsForBot 1 "Hanoi"  "HCMC"  "Da Nang"))
(display
 (string-append "Instructions for Michael the Bot:\n"
                steps
                "\n...expecting\n"
                "Move the top disk from Hanoi to HCMC.\n"
                separator
                )
 )


; test 1: next larger case, which is the smallest recursive case
(define steps (instructionsForBot 2 "Kingman"  "Barstow"  "San Bernardino"))
(define expectation
  (string-append
   "Move the top disk from Kingman to San Bernardino.\n"
   "Move the top disk from Kingman to Barstow.\n"
   "Move the top disk from San Bernardino to Barstow.\n"
   ))
(display
 (string-append "Instructions for Michael the Bot:\n"
                steps
                "\n...expecting\n"
                expectation
                separator
                )
 )

; test 2: 3 disks
(define steps (instructionsForBot 3 "Hanoi" "HCMC" "Da Nang"))
(define expectation
  (string-append
   "Move the top disk from Hanoi to HCMC.\n"
   "Move the top disk from Hanoi to Da Nang.\n"
   "Move the top disk from HCMC to Da Nang.\n"
   "Move the top disk from Hanoi to HCMC.\n"
   "Move the top disk from Da Nang to Hanoi.\n"
   "Move the top disk from Da Nang to HCMC.\n"
   "Move the top disk from Hanoi to HCMC.\n"
   ))
(display
 (string-append "Instructions for Michael the Bot:\n"
                steps
                "...expecting\n"
                expectation
                separator
                )
 )
