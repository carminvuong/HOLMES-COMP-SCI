; hw50: recurse solo
; Carmin Vuong <mvuong40@stuy.edu>
; worked with no one
; advised by no one

; This program finds the sum of integers from start to end
; parameters have to be integers
; start has to be less than or equal to end

(define sumOfConsecInts
  (lambda (start end)
    (if (= end start)
        end
        (+ end (sumOfConsecInts start (- end 1))
           )
        )
    )
  )


; proof the code works
(display (+ 0 (sumOfConsecInts 1 20)))



