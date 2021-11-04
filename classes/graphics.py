class Grapher:
    def __init__(self, 
                 train, test, 
                 figsize = (11,5), target_colors = {0:'gray',1:'red'}
                 ):         

        self.df_original = (train,test)
        self.df = train
        self.target = train['default_12m']

        self.test = test

        self.plt_figsize = figsize
        self.plt_target_colors = target_colors
    
    def scatter(self,
                x_name = 'ar_management_expenses', y_name = 'ar_net_profit',
                alpha = 0.3
                ):
        
        fig, ax = plt.subplots(figsize=self.plt_figsize)

        ax.scatter(
                x = self.df[x_name], 
                y = self.df[y_name], 
                c = self.target.map(colors),
                alpha = alpha
                )
        # ax.set_xscale('log')
        # ax.set_yscale('log')
        plt.xlabel(x_name)
        plt.ylabel(y_name)

        plt.show()

    def hist(self, 
             n_bins = 10):

        # fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

        # colors = ['red', 'tan', 'lime']
        # ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)
        # ax0.legend(prop={'size': 10})
        # ax0.set_title('bars with legend')

        # ax1.hist(x, n_bins, density=True, histtype='bar', stacked=True)
        # ax1.set_title('stacked bar')

        # ax2.hist(x, n_bins, histtype='step', stacked=True, fill=False)
        # ax2.set_title('stack step (unfilled)')
