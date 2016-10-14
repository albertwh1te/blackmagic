#lang planet neil/sicp
(define (print-point p)
        (newline)
        (display "(")
        (display (x-point p))
        (display ",")
        (display (y-point p))
        (display ")"))


(define (make-point x y) (cons x y))
(define (x-point x) (car x))
(define (y-point x) (cdr x))

(define (make-segment a b)(cons a b))
(define (start-segment v)(car v))
(define (end-segment v)(cdr v))

(define (mid-segment v)
        (cons
          (/(+ (car (car v)) (car (cdr v))) 2)
          (/(+ (cdr (car v)) (cdr (cdr v))) 2)))
          



