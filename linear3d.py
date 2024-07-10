from manimlib import *
from sympy import *

class LinearTransformation3D(ThreeDScene):

    CONFIG = {
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "basis_i_color": GREEN,
        "basis_j_color": RED,
        "basis_k_color": GOLD
    }


    def construct(self):
        a = 5
        

        M = np.array([
            [1, 6, 0],
            [0, 2, 0],
            [0, 0, 4]
        ])

        # M = np.array([[1, 6, 0],
        #               [0, 1, 0],
        #               [0, 0, 1]])

        axes = ThreeDAxes()
        axes.set_color(GREY)
        axes.add(axes.get_axis_labels())


        # basis vectors i,j,k
        basis_vector_helper = TexText("$i$", ",", "$j$", ",", "$k$")
        basis_vector_helper[0].set_color(GREEN)
        basis_vector_helper[2].set_color(RED)
        basis_vector_helper[4].set_color(GOLD)

        basis_vector_helper.to_corner(UP + RIGHT)


        # matrix


        # axes & camera
        self.add(axes)

        cube = Cube(side_length=1, color=BLUE, opacity=1)

        i_vec = Vector(np.array([1, 0, 0]), color=GREEN)
        j_vec = Vector(np.array([0, 1, 0]), color=RED)
        k_vec = Vector(np.array([0, 0, 1]), color=GOLD)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=GREEN)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=RED)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=GOLD)

        self.play(
            ShowCreation(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)
