; Carmin Vuong <mvuong40@stuy.edu>
; hw27
; worked with no one
; advised by no one


; building and displaying the procedure
(display (lambda (x y) (/ (+ x y) 2)))

(display "\n")

; first invocation
(display (
          (lambda (x y) (/ (+ x y) 2)) ; function
          3 5)                         ; arguments
         )

(display "\n")

; second invocation
(display (
          (lambda (x y) (/ (+ x y) 2)) ; function
          (sqrt 2)                     ; first argument
          (sin (/ 3.14159 4)           ; second argument
               )
          )
         )