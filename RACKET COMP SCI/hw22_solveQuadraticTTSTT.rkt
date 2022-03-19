; Carmin Vuong <mvuong40@stuy.edu>
; hw 22
; worked with no one 
; advised by no one


; the quadratic equation of interest:
;   -0.618x^2 + 1.618x + 1.732 = 0

; definitions of a, b, c, and discriminant_sqrt

(define a -0.618)
(define b 1.618)
(define c 1.732)
(define discriminant_sqrt (sqrt (- (expt b 2) (* 4 a c)) ))


(display "One solution is approximately ")
(display (/
          (+ (- b)
             discriminant_sqrt
             )
          2 a
          )
         )
(display "\n\n")

(display "The other solution is approximately ")
(display (/
          (- (- b)
             discriminant_sqrt
             )
          2 a
          )
         )

(display "\n\n")

; new quadratic equation is:
; 2.71828x^2 + 7.64x + 1.716 = 0

; new definitions for a, b, and c

(define a 2.71828)
(define b 7.64)
(define c 1.616)
(define discriminant_sqrt (sqrt (- (expt b 2) (* 4 a c)) ))

(display "One solution is approximately ")
(display (/
          (+ (- b)
             discriminant_sqrt
             )
          2 a
          )
         )
(display "\n\n")

(display "The other solution is approximately ")
(display (/
          (- (- b)
             discriminant_sqrt
             )
          2 a
          )
         )

