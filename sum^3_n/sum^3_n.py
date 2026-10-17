from manim import*
class L(ThreeDScene):
    def construct(self):
        
        
        mi=Text("Nicomachus's Theorem",
                font="times new roman",
                font_size=70).set_color_by_gradient(PURPLE,BLUE,WHITE)
        self.play(GrowFromCenter(mi))
        
        cb=Cube(side_length=0.5).set_fill(BLUE,opacity=1).set_stroke(BLACK,width=2).shift(LEFT*5)
        
        
        
        cb2=cb.copy().set_fill(YELLOW).shift(RIGHT*2)
        c2=cb2.copy().shift(IN*0.5)

        c2l=VGroup(c2,cb2)

        c2r=c2l.copy().shift(RIGHT*0.5)

        c2u=VGroup(c2r,c2l).copy().shift(UP*0.5)

        C2=VGroup(c2u,c2r,c2l).rotate(angle=-PI/3,axis=UP).rotate(angle=PI/6,axis=RIGHT)


        cb3=cb.copy().shift(RIGHT*5).set_fill(RED)
        c31=cb3.copy().shift(RIGHT*0.5)
        c32=c31.copy().shift(RIGHT*0.5)
        c3=VGroup(cb3,c31,c32)
        c331=c3.copy().shift(IN*0.5)
        c332=c331.copy().shift(IN*0.5)

        c3l=VGroup(c3,c331,c332)
        #t2
        c3i=c3l.copy().shift(UP*0.5)
        #t3
        c3r=c3i.copy().shift(UP*0.5)

        C3=VGroup(c3l,c3i,c3r).rotate(angle=-PI/3,axis=UP).rotate(angle=PI/6,axis=RIGHT)


        cb4=cb.copy().shift(RIGHT*9).set_fill(GREEN)
        c41=cb4.copy().shift(RIGHT*0.5)
        c42=c41.copy().shift(RIGHT*0.5)
        c43=c42.copy().shift(RIGHT*0.5)
        c4=VGroup(cb4,c41,c42,c43)
        c4u=c4.copy().shift(IN*0.5)

        cv4=VGroup(c4,c4u)

        c4u2=cv4.copy().shift(IN*1)
        
        cv4i=VGroup(c4u2,cv4)

        c4i=cv4i.copy().shift(UP*0.5)

        c4i2=c4i.copy().shift(UP*0.5)

        c4i3=c4i.copy().shift(UP*1)

        C4=VGroup(c4i,cv4i,c4i2,c4i3).rotate(angle=-PI/3,axis=UP).rotate(angle=PI/6,axis=RIGHT)
        
        
        #xanh 2
        v1=cb.copy().shift(RIGHT*5)
        
        cb.rotate(angle=-PI/3,axis=UP).rotate(angle=PI/6,axis=RIGHT)

        v2=v1.copy().set_fill(YELLOW).shift(IN*0.5)
        v2i=v2.copy().shift(IN*0.5)
        #2 vàng trong
        v2o=VGroup(v2,v2i)

        v2r=v2o.copy().shift(RIGHT*0.5)
        v2r2=v2r.copy().shift(RIGHT*0.5)
        # 4 vàng
        v2rg=VGroup(v2r,v2r2)
        #2 vàng ngoài
        v2l=v2o.copy().shift(RIGHT*0.75+OUT*0.75).rotate(PI/2,UP)

        V2=VGroup(v2l,v2rg,v2o)
        #đỏ giữa
        v3=VGroup(v1,V2).copy().set_fill(RED).shift(IN*1.5+RIGHT*1.5)
        #đỏ trái
        v3l=v3.copy().shift(LEFT*1.5)
        #đỏ ngoài
        v3o=v3.copy().shift(OUT*1.5)

        V3=VGroup(v3,v3l,v3o)

        v4=VGroup(v2rg,v2l).copy()
        v4u=v2l.copy().shift(IN*1.5)
        #lục lẻ trong
        s4i=VGroup(v4,v4u).shift(IN*3+RIGHT*1.5).set_fill(GREEN)

        s4l=s4i.copy().shift(LEFT*1)
        s4l1=s4l.copy().shift(LEFT*1)
        #4 lục trong
        v4l=VGroup(s4l,s4l1)

        #lục ngoài
        v4o=v4l.copy().shift(OUT*3+RIGHT*3)

        #lục giữa
        v4n=v4o.copy().shift(IN*3)

        #lục lẻ giữa
        s4in=s4i.copy().rotate(PI/2,UP).shift(RIGHT*1.5+OUT*1.5)
        
        V4=VGroup(v4l,s4i,v4o,v4n,s4in)


        v=VGroup(v1,V2,V3,V4).rotate(angle=-PI/3,axis=UP).rotate(angle=PI/6,axis=RIGHT).move_to([0,0,0])
        C4.move_to([0,0,0]).shift(RIGHT*4)
        C3.move_to([0,0,0])
        C2.move_to([0,0,0])
        cb.move_to([0,0,0]).scale(2)
        
        

        t1=MathTex(r"1^3").shift(UP*2.5).set_color(BLUE)
        t2=MathTex(r"+",
                  r"2^3").next_to(t1,RIGHT,buff=0)
        t2[1].set_color(YELLOW)
        f12=VGroup(t1,t2)
        
        t3=MathTex(r"+"
                   ,r"3^3").next_to(f12,RIGHT,buff=-0.3)
        t3[1].set_color(RED)
        f23=VGroup(f12,t3)

        t4=MathTex(r"+...+",
                   r"n^3").next_to(f23,buff=-0.3)
        t4[1].set_color(GREEN)
        f34=VGroup(f12,f23,t4)

        self.play(mi.animate.shift(UP*3.5).scale(0.7),
                  GrowFromCenter(cb)
                )
        self.play(Write(t1))
        self.wait(0.5)
        self.play(Write(t2),
                  f12.animate.move_to([0,2.5,0]),
                  cb.animate.scale(0.5).shift(LEFT*2),
                  GrowFromCenter(C2))
        self.wait(0.5)
        self.play(GrowFromCenter(C3),
                  VGroup(C2,cb).animate.shift(LEFT*3),
                  Write(t3),
                  f23.animate.move_to([0,2.5,0]))
        self.wait(0.5)
        self.play(Write(t4),
                  f34.animate.move_to([0,2.5,0]),
                  GrowFromCenter(C4))
        
        self.play(
                  C3.animate.shift(RIGHT*-3),
                  C2.animate.shift(RIGHT*-2),
                  cb.animate.shift(LEFT))
        self.add(cb,C2,C3,C4)
        self.play(cv4.animate.move_to(s4in),
                  Transform(c4u2,s4i.copy()),
                  c4i.animate.move_to(v4l),
                  c4i2.animate.move_to(v4o),
                  c4i3.animate.move_to(v4n))
        
        self.play(c3l.animate.move_to(v3l),
                  c3i.animate.move_to(v3),
                  c3r.animate.move_to(v3o))
        
        self.play(c2u.animate.move_to(v2rg),
                  Transform(c2r,v2l.copy()),
                  c2l.animate.move_to(v2o)
                  )
        self.play(cb.animate.move_to(v1))
        p=MathTex(r"1",
                   r"+",
                   r"2",
                   r"+",
                   r"3",
                   r"+...+",r"n")
        p[0].set_color(BLUE)
        p[2].set_color(YELLOW)
        p[4].set_color(RED)
        p[6].set_color(GREEN)
        
        
        p.rotate(angle=-PI/3,axis=UP).rotate(angle=PI/6,axis=RIGHT).shift(LEFT*2.75+DOWN).scale(1.3).set_opacity(2)
        self.play(Write(p),f34.animate.shift(LEFT*2.5))
        self.wait(0.5)

        of=MathTex(r"=(1+2+3+...+n)^2").next_to(f34,buff=0.1).set_color(YELLOW)
        
        self.play(Transform(p,of.copy()))
        self.wait(0.5)
        self.play(FadeOut(cb,C2,C3,C4),VGroup(f34,p).animate.move_to([0,0,0]))
        o1=MathTex(r"=\left( \frac{n(n+1)}{2} \right)^2").next_to(f34,buff=0.1).set_color(YELLOW)
        self.wait(0.5)
        self.play(Transform(p,o1) )
        self.play(VGroup(f34,p).animate.move_to([0,0,0]).scale(1.3))
        box=SurroundingRectangle(VGroup(f34,p),corner_radius=0.1,buff=0.5).set_color([PURPLE,BLUE,WHITE])
        self.play(Create(box))

        self.wait()
        return super().construct()