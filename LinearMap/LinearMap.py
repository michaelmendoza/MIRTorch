"""
Linear Operator implementations.
"""
import torch



class Linearmap():
    '''
        Our major difference with Sigpy is that:
         In sigpy, for each linear op, they IMPLEMENTED it case by case. So each instance inherit Linop()
         In out, we directly call the forward and backward ops. Which is provided by 3rd package.

         Alternative: you can try using the nn.module as the base class. It also support manual forward() and backward()
    '''
    def __init__(self, size_in, size_out, forward_op, adjoint_op):
        '''
        For initilization, this can be provided:
        size_in: the size of the input of the linear map
        size_out: ...
        '''
        self. size_in = size_in
        self.size_out = size_out
        self.forward_op = forward_op
        self.adjoint_op = adjoint_op

        class forward(torch.autograd.Function):
            @staticmethod
            def forward(ctx, data_in):
                return self.forward_op(data_in)
            @staticmethod
            def backward(ctx, grad_data_in):
                return self.adjoint_op(grad_data_in)
        self._apply = forward.apply # THis may look wired to you. But the torch.autograd.Function requires .apply
        class adjoint(torch.autograd.Function):
            @staticmethod
            def forward(ctx, data_in):
                return self.adjoint_op(data_in)
            @staticmethod
            def backward(ctx, grad_data_in):
                return self.forward_op(grad_data_in)
        self._adjoint_apply = adjoint.apply
    def check_device(self): # Make sure that the input and output and forwardop, adjop are on the same divice (CPU/CPU)
    def __call__(self):
    def __add__(self, other): # you can try the sigpy approach or your own one
    def __matmul__(self, other):
    def __sub__(self, other):
    def __neg__(self):
    @property
    def H(self):
    def _combine_compose_linops(linops):

