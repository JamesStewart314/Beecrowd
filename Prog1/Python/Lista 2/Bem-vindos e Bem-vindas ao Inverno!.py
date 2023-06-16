from math import fabs
A, B, C = map(int, input().split())
if A > B and C >= B:
    print(':)')
if B > A and B >= C:
    print(':(')
if C > B > A and fabs(C-B) < fabs(B-A):
    print(':(')
if C > B > A and fabs(C-B) >= fabs(B-A):
    print(':)')
if A > B > C and fabs(B-C) < fabs(A-B):
    print(':)')
if A > B > C and fabs(B-C) >= fabs(A-B):
    print(':(')
if A == B and C > B:
    print(':)')
if A == B and C <= B:
    print(':(')
