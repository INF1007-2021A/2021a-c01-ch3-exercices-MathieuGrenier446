#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    return a**1/2


def square(a: float) -> float:
    return pow(a,2)


def average(a: float, b: float, c: float) -> float:
    return (a+b+c)/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return (angle_degs+angle_mins/60+angle_secs/3600)*(math.pi)/180


def to_degrees(angle_rads: float) -> tuple:
    angle_dec = angle_rads*180/(math.pi)
    
    angle_degs=angle_dec
    angle_mins=(angle_degs-int(angle_degs))*60
    angle_secs=(angle_mins-int(angle_mins))*60
    return int(angle_degs), int(angle_mins), int(angle_secs)


def to_celsius(temperature: float) -> float:
    return 5/9*(temperature-32)


def to_farenheit(temperature: float) -> float:
    return 9/5*temperature+32


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
