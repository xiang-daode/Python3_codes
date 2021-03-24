# coding:utf-8

import sys
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

PI = 3.14159265
t = 0  # 动画时间参数

# #############  绘制四边形,配置四个角的颜色以实现渐变色  ################
def Quat4bgr(p0, p1, p2, p3, bgr0, bgr1, bgr2, bgr3):
    glBegin(GL_QUADS)
    glColor3f(bgr0[0], bgr0[1], bgr0[2])
    glVertex3f(p0[0], p0[1], p0[2])
    glColor3f(bgr1[0], bgr1[1], bgr1[2])
    glVertex3f(p1[0], p1[1], p1[2])
    glColor3f(bgr2[0], bgr2[1], bgr2[2])
    glVertex3f(p2[0], p2[1], p2[2])
    glColor3f(bgr3[0], bgr3[1], bgr3[2])
    glVertex3f(p3[0], p3[1], p3[2])
    glEnd()


# #############  绘制四边形,只单一颜色  ################
def drawQuat(p0, p1, p2, p3, bgr):
    glColor3f(bgr[0], bgr[1], bgr[2])
    glBegin(GL_QUADS)
    glVertex3f(p0[0], p0[1], p0[2])
    glVertex3f(p1[0], p1[1], p1[2])
    glVertex3f(p2[0], p2[1], p2[2])
    glVertex3f(p3[0], p3[1], p3[2])
    glEnd()


# ###########  立体对象建构-球体  ############
def drawBall(r):
    d = 10
    pts = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    u, v = [1, 1, 0, 0], [0, 1, 1, 0]
    for f in range(-90, 90 + d, d):
        for t in range(-180, 180 + d, d):
            for i in range(4):
                a = PI * (t + u[i] * d) / 180
                b = PI * (f + v[i] * d) / 180
                # #############  立体对象建构区  ###############
                pts[i] = [
                    r * np.cos(a) * np.cos(b),
                    r * np.sin(a) * np.cos(b),
                    r * np.sin(b)]
                bgr = [0.5 + 0.5 * np.cos(a),
                       0.5 + 0.5 * np.cos(b),
                       0.5 + 0.5 * np.cos(a + b)]

            drawQuat(pts[0], pts[1], pts[2], pts[3], bgr)  # 四边形

# ###########  立体对象建构-柱体  ############
def drawBar(r, L):
    d = 60
    pts = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    u, v = [0, 0, 1, 1], [0, 1, 1, 0]
    for f in range(-1, 2):
        for t in range(-180, 180 + d, d):
            for i in range(4):
                a = PI * (t + u[i] * d) / 180
                b = L * (0.5 + f - v[i]) / 3
                # #############  立体对象建构区  ###############
                pts[i] = [
                    r * np.cos(a),
                    r * np.sin(a),
                    b]
                bgr = [0.5 + 0.5 * np.cos(a),
                       0.5 + 0.5 * np.cos(b),
                       0.5 + 0.5 * np.cos(a + b)]

            drawQuat(pts[0], pts[1], pts[2], pts[3], bgr)  # 四边形

# ###########  立体对象建构-锥体  ############
def drawV(r, L):  # 1 cylinder
    d = 60
    pts = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    u, v = [0, 0, 1, 1], [0, 1, 1, 0]
    for f in range(0, 1):
        for t in range(-180, 180 + d, d):
            for i in range(4):
                a = PI * (t + u[i] * d) / 180
                b = L * (1 + f - v[i]) / 3
                # #############  立体对象建构区  ###############
                if v[i] == 0:
                    pts[i] = [
                        0 * r * np.cos(a),
                        0 * r * np.sin(a),
                        b]
                else:
                    pts[i] = [
                        r * np.cos(a),
                        r * np.sin(a),
                        b]
                bgr = [0.5 + 0.5 * np.cos(a),
                       0.5 + 0.5 * np.cos(b),
                       0.5 + 0.5 * np.cos(a + b)]

            drawQuat(pts[0], pts[1], pts[2], pts[3], bgr)  # 四边形

# ###########  立体对象建构-三锥体  ############
def draw3V(r, L):  # 3 cylinder
    d = 60
    pts = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    u, v = [0, 0, 1, 1], [0, 1, 1, 0]
    for f in range(0, 3):
        for t in range(-180, 180 + d, d):
            for i in range(4):
                a = PI * (t + u[i] * d) / 180
                b = L * (1 + f - v[i]) / 3
                # #############  立体对象建构区  ###############
                if v[i] == 0:
                    pts[i] = [
                        0 * np.cos(a),
                        0 * np.sin(a),
                        b]
                else:
                    pts[i] = [
                        r * np.cos(a),
                        r * np.sin(a),
                        b]
                bgr = [0.5 + 0.5 * np.cos(a),
                       0.5 + 0.5 * np.cos(b),
                       0.5 + 0.5 * np.cos(a + b)]

            drawQuat(pts[0], pts[1], pts[2], pts[3], bgr)  # 四边形


# ############  绘制所有对象  ###############

def drawAll():
    global t
    # 清除之前画面:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glPolygonMode(GL_FRONT, GL_FILL)
    glLoadIdentity()
    glTranslatef(0, -0.25, 0)
    glRotatef(75, 0.8, 0, 0)  # (角度,x,y,z)

    Quat4bgr([-1, -1, 0], [1, -1, 0], [0.25, 1, 0], [-0.25, 1, 0],
             [0, .2, .6], [0, .6, .2], [.1, .1, .1], [.1, .1, .1])

    # 全局自动旋转:
    glPushMatrix()
    glRotatef(t / 3, 0, 0, 1)  # (角度,x,y,z)
    # ################  调用各对象绘图函数  #################### #

    drawBall(0.3 + .25 * np.sin(t / 13))  # 球体

    # 自由活动体-1 ==================
    glPushMatrix()
    glRotatef(t, 0, 1, 0)
    glTranslatef(.5 * np.cos(t / 60.0), 0, 0.15)
    drawBar(0.12 + .1 * np.sin(t / 30), .6)
    glPopMatrix()
    # ==================================

    # 自由活动体-2 ==================
    glPushMatrix()
    glRotatef(t, 0, 0, 1)
    glTranslatef(0, 0.15, .5 * np.cos(t / 100.0))
    drawV(0.1, 0.8 + .6 * np.sin(t / 20))  # 1 cylinder
    glPopMatrix()
    # ==================================

    # 自由活动体-3 ==================
    glPushMatrix()
    glRotatef(t, .5, 0, 0.3)
    glTranslatef(0, .5 * np.cos(t / 100.0), 0.15)
    draw3V(0.1, 1)  # 3 cylinder
    glPopMatrix()
    # ==================================


    glPopMatrix()
    #####################################

    # 刷新显示:
    glFlush()
    t = t + 1


# ################## 初始化OpenGL  ##########################
def main():
    # 使用glut初始化OpenGL:
    glutInit()

    # 显示模式:GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)

    # 窗口位置及大小-生成:
    glutInitWindowPosition(200, 0)
    glutInitWindowSize(900, 900)
    glutCreateWindow(b"OpenGL in Python   ---by daode1212")

    # 调用函数绘制图像:
    glutDisplayFunc(drawAll)

    # 产生动画函数:
    glutIdleFunc(drawAll)

    # 主循环:
    glutMainLoop()


# ######################  调用主入口函数  ##########################
main()
