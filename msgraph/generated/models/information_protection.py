from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import bitlocker, data_loss_prevention_policy, entity, information_protection_policy, sensitivity_label, sensitivity_policy_settings, threat_assessment_request

from . import entity

@dataclass
class InformationProtection(entity.Entity):
    # The bitlocker property
    bitlocker: Optional[bitlocker.Bitlocker] = None
    # The dataLossPreventionPolicies property
    data_loss_prevention_policies: Optional[List[data_loss_prevention_policy.DataLossPreventionPolicy]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy property
    policy: Optional[information_protection_policy.InformationProtectionPolicy] = None
    # The sensitivityLabels property
    sensitivity_labels: Optional[List[sensitivity_label.SensitivityLabel]] = None
    # The sensitivityPolicySettings property
    sensitivity_policy_settings: Optional[sensitivity_policy_settings.SensitivityPolicySettings] = None
    # The threatAssessmentRequests property
    threat_assessment_requests: Optional[List[threat_assessment_request.ThreatAssessmentRequest]] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import bitlocker, data_loss_prevention_policy, entity, information_protection_policy, sensitivity_label, sensitivity_policy_settings, threat_assessment_request

        fields: Dict[str, Callable[[Any], None]] = {
            "bitlocker": lambda n : setattr(self, 'bitlocker', n.get_object_value(bitlocker.Bitlocker)),
            "dataLossPreventionPolicies": lambda n : setattr(self, 'data_loss_prevention_policies', n.get_collection_of_object_values(data_loss_prevention_policy.DataLossPreventionPolicy)),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(information_protection_policy.InformationProtectionPolicy)),
            "sensitivityLabels": lambda n : setattr(self, 'sensitivity_labels', n.get_collection_of_object_values(sensitivity_label.SensitivityLabel)),
            "sensitivityPolicySettings": lambda n : setattr(self, 'sensitivity_policy_settings', n.get_object_value(sensitivity_policy_settings.SensitivityPolicySettings)),
            "threatAssessmentRequests": lambda n : setattr(self, 'threat_assessment_requests', n.get_collection_of_object_values(threat_assessment_request.ThreatAssessmentRequest)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    

