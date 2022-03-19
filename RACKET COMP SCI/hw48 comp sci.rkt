; hw 48: nowtasial
; Carmin Vuong <mvuong40@stuy.edu>
; worked with no one
; advised by no one

; I am asked to calculate
; the number of possible arrangements n students can make in a line.
(define nowtasial
  (lambda
      (studentCount)
    (if (= studentCount 1)
        1 ; base case
        (* studentCount (nowtasial (- studentCount 1))) ; recursive case
        )
    )
  )


(display "number of total arrangements: ")
(display (nowtasial 4))