from manim import *
# Manim Community v0.17+ API
# Visual explanation for LeetCode: Best Time to Buy and Sell Stock II

class StockProfitScene(Scene):
    def construct(self):
        title = Title("Best Time to Buy and Sell Stock II", subtitle="LeetCode - Visual Explanation")
        self.play(Write(title))
        self.wait(0.8)

        example = Tex("Input: prices = [7, 1, 5, 3, 6, 4]", font_size=36)
        output = Tex("Output: 7", font_size=36)
        example_group = VGroup(example, output).arrange(DOWN, buff=0.25).to_edge(UP)
        example_group.shift(DOWN * 0.2)
        self.play(FadeIn(example_group, shift=DOWN))
        self.wait(0.6)

        prices = [7, 1, 5, 3, 6, 4]
        boxes = VGroup()
        for i, p in enumerate(prices):
            rect = Rectangle(width=1.0, height=1.0, stroke_width=2)
            rect.set_fill(GREY_BROWN, opacity=0.08)
            txt = Tex(str(p), font_size=30).move_to(rect.get_center())
            box = VGroup(rect, txt)
            box.shift(RIGHT * i * 1.25)
            boxes.add(box)

        boxes.move_to(ORIGIN + DOWN * 0.1)
        self.play(LaggedStartMap(FadeIn, boxes, shift=UP, lag_ratio=0.12), run_time=1.0)
        self.wait(0.4)

        indices = VGroup(*[Tex(str(i), font_size=20).next_to(boxes[i], DOWN, buff=0.12) for i in range(len(prices))])
        self.play(LaggedStartMap(FadeIn, indices, lag_ratio=0.05))
        self.wait(0.3)

        profit_text = Tex("Profit = 0", font_size=28).to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.4)
        self.play(FadeIn(profit_text))
        self.wait(0.25)

        algo_text = Tex("Rule: add every positive difference (prices[i] - prices[i-1])", font_size=22)
        algo_text.to_corner(UL)
        self.play(FadeIn(algo_text))
        self.wait(0.5)

        pointer = Arrow(UP * 0.7, DOWN * 0.05).next_to(boxes[0], UP)
        pointer_text = Tex("i = 1", font_size=20).next_to(pointer, UP)
        self.play(GrowArrow(pointer), FadeIn(pointer_text))
        self.wait(0.3)

        total_profit = 0
        for i in range(1, len(prices)):
            new_pointer = pointer.copy().next_to(boxes[i], UP)
            new_pointer_text = Tex(f"i = {i}", font_size=20).next_to(new_pointer, UP)
            self.play(Transform(pointer, new_pointer), Transform(pointer_text, new_pointer_text), run_time=0.45)

            diff = prices[i] - prices[i - 1]
            diff_sign = "+" if diff > 0 else ""
            diff_text = Tex(f"prices[{i}] - prices[{i-1}] = {diff_sign}{diff}", font_size=22)
            diff_text.next_to(algo_text, DOWN)

            self.play(LaggedStart(Indicate(boxes[i - 1], scale_factor=1.05), Indicate(boxes[i], scale_factor=1.05)), run_time=0.55)
            self.play(FadeIn(diff_text))
            self.wait(0.35)

            if diff > 0:
                buy_mark = Tex("BUY", font_size=20, color=GREEN).next_to(boxes[i - 1], DOWN, buff=0.25)
                sell_mark = Tex("SELL", font_size=20, color=RED).next_to(boxes[i], DOWN, buff=0.25)
                inc = Tex(f"+{diff}", font_size=26).next_to(boxes[i], UP)
                self.play(FadeIn(buy_mark), FadeIn(sell_mark))
                self.wait(0.2)
                self.play(GrowFromCenter(inc))
                total_profit += diff
                new_profit = Tex(f"Profit = {total_profit}", font_size=28).to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.4)
                self.play(Transform(profit_text, new_profit))
                self.wait(0.2)
                self.play(FadeOut(buy_mark), FadeOut(sell_mark), FadeOut(inc))
            else:
                no_gain = Tex("No gain", font_size=20).next_to(diff_text, DOWN)
                self.play(FadeIn(no_gain))
                self.wait(0.25)
                self.play(FadeOut(no_gain))

            self.play(FadeOut(diff_text))
            self.wait(0.12)

        final = Tex(f"Final Profit = {total_profit}", font_size=36, color=YELLOW)
        final.move_to(DOWN * 1.8)
        self.play(FadeIn(final, shift=UP))
        self.wait(0.8)

        rule = BulletedList("Take every positive difference between consecutive days.", "Time: O(n)", "Space: O(1)", dot_scale=0.6)
        rule.to_edge(DOWN)
        self.play(FadeIn(rule))
        self.wait(1.0)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.0)
        end = Text("Thanks! Good luck 🙂", font_size=34)
        self.play(Write(end))
        self.wait(1.2)
