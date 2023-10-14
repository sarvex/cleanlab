from cleanlab.datalab.internal.adapter.imagelab import (
    ImagelabIssueFinderAdapter,
    ImagelabDataIssuesAdapter,
    ImagelabReporterAdapter,
)
from cleanlab.datalab.internal.data_issues import DataIssues
from cleanlab.datalab.internal.issue_finder import IssueFinder
from cleanlab.datalab.internal.report import Reporter


def issue_finder_factory(imagelab):
    return ImagelabIssueFinderAdapter if imagelab else IssueFinder


def data_issues_factory(imagelab):
    return ImagelabDataIssuesAdapter if imagelab else DataIssues


def report_factory(imagelab):
    return ImagelabReporterAdapter if imagelab else Reporter
