; hw 49: fibonacci rabbits
; Carmin Vuong <mvuong40@stuy.edu>
; worked with no one
; advised by no one

; testing comparison procedures other than =
(display (> 5 3))    (display "\n")
(display (<= 4 4))   (display "\n")
(display (< 4 4))    (display "\n")  (display "\n")

(define fib
  (lambda
      (month)
    (if (<= month 2)
        1
        (+ (fib (- month 1))
           (fib (- month 2))
           )
      )
    )
  )

; test cases
(display (fib 1)) (display "\n") ; 1
(display (fib 4)) (display "\n") ; 3
(display (fib 19)) (display "\n") ; 4181