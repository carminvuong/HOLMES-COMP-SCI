#|  Carmin Vuong <mvuong40@stuy.edu>
    hw34
    worked with no one
    advised by no one
|#

; the 2 procedures (oneSolution and otherSolution)
(define oneSolution (lambda (a b c discriminant_sqrt)
  (/
          (+ (- b)
             discriminant_sqrt
             )
          2 a  ; n-ary division! numerator/ (2*a) = numerator/2/a
          )
        )
)
(define otherSolution (lambda (a b c discriminant_sqrt)
  (/
          (- (- b)
             discriminant_sqrt
             )
          2 a  ; n-ary division! numerator/ (2*a) = numerator/2/a
          )
        )
)



; symbols for coefficients of the first equation,
;   -0.618x^2 + 1.618x + 1.732 = 0
(define a -0.618)
(define b 1.618 )
(define c 1.732 )
(define discriminant_sqrt (sqrt (- (* b b) (* 4 a c))) )

;; display solutions
(display "One solution is approximately ")

(display (oneSolution a b c discriminant_sqrt))

(display "\n")  

(display "The other solution is approximately ")

(display (otherSolution a b c discriminant_sqrt))

(display "\n\n")

(display "For the second equation\n")
;;   2.71828x^2 + 7.64x + 1.616 = 0

(define a 2.71828)
(define b 7.64   )
(define c 1.616  )
(define discriminant_sqrt (sqrt (- (* b b) (* 4 a c))) )

;; display the solutions
(display "One solution is approximately ")


(display (oneSolution a b c discriminant_sqrt))

(display "\n")  
;
(display "The other solution is approximately ")

(display (otherSolution a b c discriminant_sqrt))

(display "\n")
(display "\n")

; ------------------------------------------------------------------------------------
;my attempt at doing the optional extra education 



; building of aSolution
(define aSolution (lambda (solution) (solution a b c discriminant_sqrt)))

; second equation solutions
(display (aSolution oneSolution))
(display "\n")
(display (aSolution otherSolution))
(display "\n")

;redefining symbols for first equation
(define a -0.618)
(define b 1.618 )
(define c 1.732 )
(define discriminant_sqrt (sqrt (- (* b b) (* 4 a c))) )

;first equation solutions
(display (aSolution oneSolution))
(display "\n")
(display (aSolution otherSolution))

