; Carmin Vuong <mvuong40@stuy.edu>
; hw 26
; worked with no one, advised by no one


; defining and displaying the function
(display (lambda (r) ; r is the parameter
  (* r r 3.14)       ; this stuff is the instructions
 )
)


(display "\n") ; new line

; displaying the invocation of the function (#1)
(display
 (
  (lambda (r) (* r r 3.14)) ; the same function above but condensed into one line
  10                        ; argument for function (radius for circle area formula)
  )
 )

(display "\n") ; new line

; displaying the invocation of the function (#2)
(display
 (
  (lambda (r) (* r r 3.14)) ; the same function above but condensed into one line
  3                        ; argument for function (radius for circle area formula)
  )
 )

(display "\n") ; new line

; displaying the invocation of the function (#3)
(display
 (
  (lambda (r) (* r r 3.14)) ; the same function above but condensed into one line
   (+ 3 4)                       ; argument for function (radius for circle area formula)
  )
 )