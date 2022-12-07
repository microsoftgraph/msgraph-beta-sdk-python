from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

bitlocker = lazy_import('msgraph.generated.models.bitlocker')
data_loss_prevention_policy = lazy_import('msgraph.generated.models.data_loss_prevention_policy')
entity = lazy_import('msgraph.generated.models.entity')
information_protection_policy = lazy_import('msgraph.generated.models.information_protection_policy')
sensitivity_label = lazy_import('msgraph.generated.models.sensitivity_label')
sensitivity_policy_settings = lazy_import('msgraph.generated.models.sensitivity_policy_settings')
threat_assessment_request = lazy_import('msgraph.generated.models.threat_assessment_request')

class InformationProtection(entity.Entity):
    @property
    def bitlocker(self,) -> Optional[bitlocker.Bitlocker]:
        """
        Gets the bitlocker property value. The bitlocker property
        Returns: Optional[bitlocker.Bitlocker]
        """
        return self._bitlocker
    
    @bitlocker.setter
    def bitlocker(self,value: Optional[bitlocker.Bitlocker] = None) -> None:
        """
        Sets the bitlocker property value. The bitlocker property
        Args:
            value: Value to set for the bitlocker property.
        """
        self._bitlocker = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new informationProtection and sets the default values.
        """
        super().__init__()
        # The bitlocker property
        self._bitlocker: Optional[bitlocker.Bitlocker] = None
        # The dataLossPreventionPolicies property
        self._data_loss_prevention_policies: Optional[List[data_loss_prevention_policy.DataLossPreventionPolicy]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The policy property
        self._policy: Optional[information_protection_policy.InformationProtectionPolicy] = None
        # The sensitivityLabels property
        self._sensitivity_labels: Optional[List[sensitivity_label.SensitivityLabel]] = None
        # The sensitivityPolicySettings property
        self._sensitivity_policy_settings: Optional[sensitivity_policy_settings.SensitivityPolicySettings] = None
        # The threatAssessmentRequests property
        self._threat_assessment_requests: Optional[List[threat_assessment_request.ThreatAssessmentRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InformationProtection()
    
    @property
    def data_loss_prevention_policies(self,) -> Optional[List[data_loss_prevention_policy.DataLossPreventionPolicy]]:
        """
        Gets the dataLossPreventionPolicies property value. The dataLossPreventionPolicies property
        Returns: Optional[List[data_loss_prevention_policy.DataLossPreventionPolicy]]
        """
        return self._data_loss_prevention_policies
    
    @data_loss_prevention_policies.setter
    def data_loss_prevention_policies(self,value: Optional[List[data_loss_prevention_policy.DataLossPreventionPolicy]] = None) -> None:
        """
        Sets the dataLossPreventionPolicies property value. The dataLossPreventionPolicies property
        Args:
            value: Value to set for the dataLossPreventionPolicies property.
        """
        self._data_loss_prevention_policies = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bitlocker": lambda n : setattr(self, 'bitlocker', n.get_object_value(bitlocker.Bitlocker)),
            "data_loss_prevention_policies": lambda n : setattr(self, 'data_loss_prevention_policies', n.get_collection_of_object_values(data_loss_prevention_policy.DataLossPreventionPolicy)),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(information_protection_policy.InformationProtectionPolicy)),
            "sensitivity_labels": lambda n : setattr(self, 'sensitivity_labels', n.get_collection_of_object_values(sensitivity_label.SensitivityLabel)),
            "sensitivity_policy_settings": lambda n : setattr(self, 'sensitivity_policy_settings', n.get_object_value(sensitivity_policy_settings.SensitivityPolicySettings)),
            "threat_assessment_requests": lambda n : setattr(self, 'threat_assessment_requests', n.get_collection_of_object_values(threat_assessment_request.ThreatAssessmentRequest)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def policy(self,) -> Optional[information_protection_policy.InformationProtectionPolicy]:
        """
        Gets the policy property value. The policy property
        Returns: Optional[information_protection_policy.InformationProtectionPolicy]
        """
        return self._policy
    
    @policy.setter
    def policy(self,value: Optional[information_protection_policy.InformationProtectionPolicy] = None) -> None:
        """
        Sets the policy property value. The policy property
        Args:
            value: Value to set for the policy property.
        """
        self._policy = value
    
    @property
    def sensitivity_labels(self,) -> Optional[List[sensitivity_label.SensitivityLabel]]:
        """
        Gets the sensitivityLabels property value. The sensitivityLabels property
        Returns: Optional[List[sensitivity_label.SensitivityLabel]]
        """
        return self._sensitivity_labels
    
    @sensitivity_labels.setter
    def sensitivity_labels(self,value: Optional[List[sensitivity_label.SensitivityLabel]] = None) -> None:
        """
        Sets the sensitivityLabels property value. The sensitivityLabels property
        Args:
            value: Value to set for the sensitivityLabels property.
        """
        self._sensitivity_labels = value
    
    @property
    def sensitivity_policy_settings(self,) -> Optional[sensitivity_policy_settings.SensitivityPolicySettings]:
        """
        Gets the sensitivityPolicySettings property value. The sensitivityPolicySettings property
        Returns: Optional[sensitivity_policy_settings.SensitivityPolicySettings]
        """
        return self._sensitivity_policy_settings
    
    @sensitivity_policy_settings.setter
    def sensitivity_policy_settings(self,value: Optional[sensitivity_policy_settings.SensitivityPolicySettings] = None) -> None:
        """
        Sets the sensitivityPolicySettings property value. The sensitivityPolicySettings property
        Args:
            value: Value to set for the sensitivityPolicySettings property.
        """
        self._sensitivity_policy_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("bitlocker", self.bitlocker)
        writer.write_collection_of_object_values("dataLossPreventionPolicies", self.data_loss_prevention_policies)
        writer.write_object_value("policy", self.policy)
        writer.write_collection_of_object_values("sensitivityLabels", self.sensitivity_labels)
        writer.write_object_value("sensitivityPolicySettings", self.sensitivity_policy_settings)
        writer.write_collection_of_object_values("threatAssessmentRequests", self.threat_assessment_requests)
    
    @property
    def threat_assessment_requests(self,) -> Optional[List[threat_assessment_request.ThreatAssessmentRequest]]:
        """
        Gets the threatAssessmentRequests property value. The threatAssessmentRequests property
        Returns: Optional[List[threat_assessment_request.ThreatAssessmentRequest]]
        """
        return self._threat_assessment_requests
    
    @threat_assessment_requests.setter
    def threat_assessment_requests(self,value: Optional[List[threat_assessment_request.ThreatAssessmentRequest]] = None) -> None:
        """
        Sets the threatAssessmentRequests property value. The threatAssessmentRequests property
        Args:
            value: Value to set for the threatAssessmentRequests property.
        """
        self._threat_assessment_requests = value
    

