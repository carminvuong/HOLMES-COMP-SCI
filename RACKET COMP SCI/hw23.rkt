; Carmin Vuong <mvuong40@stuy.edu>
; hw23
; worked with no one
; advised by no one


; task 1d: symbols for coefficients of the first equation,
;   -0.618x^2 + 1.618x + 1.732 = 0
(define a -0.618)
(define b 1.618 )
(define c 1.732 )

; task 4: an intermediate value that will be used twice:
(define discriminant_sqrt (sqrt (- (* b b) (* 4 a c))) )

; display solutions
(display "One solution is approximately ")
(define one_solution1 (/
          (+ (- b)  ; Finally! a valuable use of negation!
             discriminant_sqrt
             )
          2 a  ; n-ary division! numerator/ (2*a) = numerator/2/a
          )
         )
(display one_solution1)
(display "\n")

; hw 23
; first equation, first answer
(display "Evaluating the quadratic expression with the alleged solution: ")
(display (+ (* a one_solution1 one_solution1) (* b one_solution1) c))
(display " ≈ 0")
(display "\n\n")

; first equation, second answer
(display "The other solution is approximately ")
(define other_solution1 (/
          (- (- b)
             discriminant_sqrt
             )
          2 a
          )
         )
(display other_solution1)
(display "\n")

(display "Evaluating the quadratic expression with the alleged solution: ")
(display (+ (* other_solution1 other_solution1 a) (* b other_solution1) c)) 
(display " ≈ 0")
(display "\n\n")


; different definitions for second equation
(define a 2.71828)
(define b 7.64)
(define c 1.616)
(define discriminant_sqrt (sqrt (- (* b b) (* 4 a c))) )


; second equation, first answer
(display "One solution for the 2nd equation is approximately ")
(define one_solution2 (/
          (+ (- b)  ; Finally! a valuable use of negation!
             discriminant_sqrt
             )
          2 a  ; n-ary division! numerator/ (2*a) = numerator/2/a
          )
         )
(display one_solution2)
(display "\n")  

(display "Evaluating the quadratic expression with the alleged solution: ")
(display (+ (* a one_solution2 one_solution2) (* b one_solution2) c))
(display " ≈ 0")
(display "\n\n")

; second equation, second answer
(display "One solution for the 2nd equation is approximately ")
(define other_solution2 (/
          (- (- b)  ; Finally! a valuable use of negation!
             discriminant_sqrt
             )
          2 a  ; n-ary division! numerator/ (2*a) = numerator/2/a
          )
         )
(display other_solution2)
(display "\n")

(display "Evaluating the quadratic expression with the alleged solution: ")
(display (+ (* a other_solution2 other_solution2) (* b other_solution2) c))
(display " ≈ 0")
