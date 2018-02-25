from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from SimPEG.EM.OldBase import BaseEMSurvey
from SimPEG.EM.Static.DC.SrcDC import BaseSrc
from SimPEG.EM.Static.DC.RxDC import BaseRx
from SimPEG.EM.Static.DC import Survey as SurveyDC


class Survey(SurveyDC):

    def __init__(self, srcList, **kwargs):
        self.srcList = srcList
        SurveyDC.__init__(self, srcList, **kwargs)

    def dpred(self, m=None, f=None):
        """
            Predicted data.

            .. math::
                d_\\text{pred} = Pf(m)
        """
        return self.prob.Jvec(m, m, f=f)
