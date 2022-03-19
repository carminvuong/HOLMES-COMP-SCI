; Carmin Vuong <mvuong40@stuy.edu>
; hw28
; worked with no one
; advised by no one

; procedure for average of 2 named averageOf2
(define averageOf2 
 (lambda (a b) 
   (/ (+ a b) 2 
      )
   )  
 )

; invocations of the anonymous procedure without violation NTTSTT
(display (averageOf2 10 2))

(display "\n")

(display (averageOf2 (sqrt 2) (sin (/ 3.14 4))))
(display "\n")

; procedure for trapezoid area named trapezoidArea
(define trapezoidArea
  (lambda
    (b1 b2 a)    ; parameters
    (* (/ (+ b1 b2) 2) a) ; expression for area of a trapezoid
   )
 )

; invocations of
(display (trapezoidArea 10 15 2))
(display "\n")
(display (trapezoidArea 456 789 234))