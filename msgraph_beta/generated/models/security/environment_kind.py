from enum import Enum

class EnvironmentKind(str, Enum):
    AzureSubscription = "azureSubscription",
    AwsOrganization = "awsOrganization",
    AwsAccount = "awsAccount",
    GcpOrganization = "gcpOrganization",
    GcpProject = "gcpProject",
    DockersHubOrganization = "dockersHubOrganization",
    DevOpsConnection = "devOpsConnection",
    AzureDevOpsOrganization = "azureDevOpsOrganization",
    GitHubOrganization = "gitHubOrganization",
    GitLabGroup = "gitLabGroup",
    JFrogArtifactory = "jFrogArtifactory",
    UnknownFutureValue = "unknownFutureValue",

