from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class InformationProtectionPolicySetting(Entity):
    # The defaultLabelId property
    default_label_id: Optional[str] = None
    # Exposes whether justification input is required on label downgrade.
    is_downgrade_justification_required: Optional[bool] = None
    # Exposes whether mandatory labeling is enabled.
    is_mandatory: Optional[bool] = None
    # Exposes the more information URL that can be configured by the administrator.
    more_info_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtectionPolicySetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtectionPolicySetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InformationProtectionPolicySetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultLabelId": lambda n : setattr(self, 'default_label_id', n.get_str_value()),
            "isDowngradeJustificationRequired": lambda n : setattr(self, 'is_downgrade_justification_required', n.get_bool_value()),
            "isMandatory": lambda n : setattr(self, 'is_mandatory', n.get_bool_value()),
            "moreInfoUrl": lambda n : setattr(self, 'more_info_url', n.get_str_value()),
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
        writer.write_str_value("defaultLabelId", self.default_label_id)
        writer.write_bool_value("isDowngradeJustificationRequired", self.is_downgrade_justification_required)
        writer.write_bool_value("isMandatory", self.is_mandatory)
        writer.write_str_value("moreInfoUrl", self.more_info_url)
    

