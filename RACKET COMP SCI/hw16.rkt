; task 0 - 1st line
(display "hw14#3a. length of other leg: ")
(display (sqrt(abs(- (expt 12 2)(expt 13 2)))))
(display " units")

; task 0 - 2nd line
(display "\n\n")

; task 0 - 3rd line
(display "hw14#3b. quotient: ")
(display (/ (/ 11 22)(- (expt 5 2.5) 123)))
(display " units")

; task 0 - 4th line
(display "\n")
(display "That's all, folks!")

; skip a line
(display "\n\n")

; the rest of the hw
(display "One solution is approximately ")
(display (/ (+ -1.618 (sqrt (- (expt 1.618 2) (* 4 -0.618 1.732)))) (* 2 -0.618)))

(display "\n\n")

(display "The other solution is approximately ")
(display (/ (- -1.618 (sqrt (- (expt 1.618 2) (* 4 -0.618 1.732)))) (* 2 -0.618)))