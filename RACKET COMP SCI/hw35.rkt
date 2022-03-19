; Carmin Vuong <mvuong40@stuy.edu>
; hw 35
; worked with no one
; advised by no one

; helper procedure to find circle area based on radius, named circleArea
(define circleArea
  (lambda (radius) (* radius radius 3.14))
 )

; building annulusArea, with help from circleArea
(define annulusArea
  (lambda (outerRadius innerRadius) ; outer circle radius first, then inner circle radius
  (- (circleArea outerRadius) (circleArea innerRadius)))
 )

; testing annulusArea
(display "testing annulusArea: ")
(display "\n")
(display (annulusArea 10 9))
(display "\n")
(display (annulusArea 18 8))
(display "\n")

; building targetArea
(define targetArea
  (lambda (innermostRadius)
  (+ (annulusArea (* innermostRadius 2) innermostRadius)
     (annulusArea (* innermostRadius 4) (* innermostRadius 3))
     (annulusArea (* innermostRadius 6) (* innermostRadius 5))
   )
 )
)

; testing targetArea
(display "\n")
(display "testing targetArea: ")
(display "\n")
(display (targetArea 1))
(display "\n")
(display (targetArea 2))
(display "\n")
(display (targetArea 3))
(display "\n")
(display (targetArea 4))
(display "\n")
(display (targetArea 5))
(display "\n")
(display (targetArea 10))
(display "\n")
(display (targetArea 20))
(display "\n")
(display (targetArea 100))




