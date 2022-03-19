(define weakAfterBoost                                 ; line 01
  (lambda (strong weak) (strongGetsMore weak strong))  ; line 02
  )                                                    ; line 03
                                                       
(define strongGetsMore                                 ; line 05
  (lambda (strong weak) (+ strong (/ weak 2)))         ; line 06
  )                                                    ; line 07

(display                                               ; line 09
 (weakAfterBoost 10 2)                                 ; line 10
 )                                                     ; line 11