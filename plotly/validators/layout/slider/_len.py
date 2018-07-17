import _plotly_utils.basevalidators


class LenValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='len', parent_name='layout.slider', **kwargs
    ):
        super(LenValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='arraydraw',
            min=0,
            role='style',
            **kwargs
        )