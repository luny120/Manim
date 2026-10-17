from manim import *

class i(Scene):
    def construct(self):
        t=Text("Quartic equation",
               font="dancing script",
               font_size=70).set_color_by_gradient(BLUE,WHITE)
        
        p=r"\frac{8ac-3b^2}{8a^2}"
        q=r"\frac{b^3-4abc+8a^2d}{8a^3}"
        r1=r"\frac{c^2-3bd+12ae}{a^2}"
        r=rf" \frac{{ -3 \left( {p} \right)^2 +4 \left( {r1} \right) }}{{8}} "
        s=rf"\sqrt{{ \frac{{ -\left( {p} \right) + \sqrt{{ \left( {p} \right)^2 -4 \left( {r} \right) }} }}{{2}} }}"
        f=MathTex(r"ax^4+bx^3+cx^2+dx+e=0").shift(UP*2.5)
        f1 = MathTex(
                           rf"x=-\frac{{b}}{{4a}} \pm \frac{{1}}{{2}} &",
                           rf"\sqrt{{{s}}}",
                           rf"\pm \frac{{1}}{{2}}",
                           rf"\sqrt{{ -\left( {s} \right) -2 \left( {p} \right) \pm \frac{{{q}}}{{\sqrt{{{s}}}}} }}"
                           
        ).shift(RIGHT*20+DOWN).set_color(YELLOW)
        self.play(GrowFromCenter(t))
        self.wait(0.5)
        self.play(t.animate.shift(UP*3.5).scale(0.7),
                  GrowFromCenter(f))
        self.wait(0.5)
        self.play(Write(f1))
        self.play(f1.animate.shift(LEFT*40)
                  ,run_time=10,rate_func=rate_functions.ease_in_out_sine)
        #self.play(solution.animate.shift(UP*9).set_color([YELLOW,PURPLE,WHITE]),run_time=5)
        self.wait(2)
