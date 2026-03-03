#!/usr/bin/env python3
import math

density_of_lead = 11.348 # g/cm3
grams_per_pound = 453.592 #g

def gauge_to_mm(gauge):
    volume_cm3  = 1. / gauge * grams_per_pound / density_of_lead
    gauge_in_cm = math.cbrt(3. * volume_cm3 / (4. * math.pi)) * 2.
    return gauge_in_cm * 10

def mm_to_gauge(lead_ball_diameter_mm: float):
    lead_ball_radius_cm = lead_ball_diameter_mm / 10. / 2.
    volume_cm3 = 4./3. * math.pi * math.pow(lead_ball_radius_cm, 3.)
    return 1. / (volume_cm3 * density_of_lead / grams_per_pound)

