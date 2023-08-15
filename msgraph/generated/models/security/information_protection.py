from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .information_protection_policy_setting import InformationProtectionPolicySetting
    from .sensitivity_label import SensitivityLabel

from ..entity import Entity

@dataclass
class InformationProtection(Entity):
    # Read the Microsoft Purview Information Protection policy settings for the user or organization.
    label_policy_settings: Optional[InformationProtectionPolicySetting] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Read the Microsoft Purview Information Protection labels for the user or organization.
    sensitivity_labels: Optional[List[SensitivityLabel]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InformationProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .information_protection_policy_setting import InformationProtectionPolicySetting
        from .sensitivity_label import SensitivityLabel

        from ..entity import Entity
        from .information_protection_policy_setting import InformationProtectionPolicySetting
        from .sensitivity_label import SensitivityLabel

        fields: Dict[str, Callable[[Any], None]] = {
            "labelPolicySettings": lambda n : setattr(self, 'label_policy_settings', n.get_object_value(InformationProtectionPolicySetting)),
            "sensitivityLabels": lambda n : setattr(self, 'sensitivity_labels', n.get_collection_of_object_values(SensitivityLabel)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("labelPolicySettings", self.label_policy_settings)
        writer.write_collection_of_object_values("sensitivityLabels", self.sensitivity_labels)
    

