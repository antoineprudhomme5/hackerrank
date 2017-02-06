(defun sum (x y)    
    (+ x y))
(setq a (read-line))
(setq b (read-line))

(write (sum (parse-integer a) (parse-integer b)))
