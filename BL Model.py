#------------------------------------------------------------
# EngSci Capstone Project 
# Black-Litterman Model 
#------------------------------------------------------------

def BL(mu, Q, targetReturn, lb, ub):
    # the objective of this function is to generate investment portfolios 
    # using Black-Litterman model per user's request

def optimize_and_display(title, names, R, C, rf, color='black'):
        # optimize
        W = solve_weights(R, C, rf)
        mean, var = port_mean_var(W, R, C)                                              # calculate tangency portfolio
        f_mean, f_var, f_weights = solve_frontier(R, C, rf)             # calculate min-var frontier

        # display min-var frontier
        print(title)
        print_assets(names, W, R, C)
        n = len(names)
        scatter([C[i,i]**.5 for i in range(n)], R, marker='x',color=color)  # draw assets
        for i in range(n):                                                                              # draw labels
                text(C[i,i]**.5, R[i], '  %s'%names[i], verticalalignment='center', color=color)
        scatter(var**.5, mean, marker='o', color=color)                 # draw tangency portfolio
        plot(f_var**.5, f_mean, color=color)                                    # draw min-var frontier
        xlabel('$\sigma$'), ylabel('$r$')
        grid(True)