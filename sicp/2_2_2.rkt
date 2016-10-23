#lang sicp
;; understand list and cons
(define a (cons (list 1 2)(list 3 4)))
(define a_s (cons (list 1 2)(cons 3 (cons 4 '()))))
;; exercise 2.24
(define w (list 1 (list 2(list 3 4))))
(display w)
;; exercise 2.25
(define a1 (list 1 3 (list 5 7) 9))
(display a1)
(newline)
(display (car(cdr(car(cdr(cdr a1))))))
(newline)
(define a2 (list (list 7)))
(display (car(car a2)))
(newline)
(define a3 (list 1(list 2 (list 3 (list 4 (list 5 (list 6 7)))))))
(display (car(cdr(car(cdr(car(cdr(car(cdr(car(cdr(car (cdr a3)))))))))))))
;; exercise 2.26
(define x (list 1 2 3))
(define y (list 4 5 6))
(display (append x y))
(newline)
(display (cons x y))
(newline)
(display (list x y))
(newline)
;; exercise 2.18
(define (reverse items)
  (if (null? (cdr(cdr items)))
                (cons (car(cdr items)) (cons (car items) '()))
                (append (reverse (cdr items)) (cons (car items) '()))))
;; exercise 2.27

