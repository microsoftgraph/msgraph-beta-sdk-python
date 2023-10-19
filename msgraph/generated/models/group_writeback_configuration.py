from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .writeback_configuration import WritebackConfiguration

from .writeback_configuration import WritebackConfiguration

@dataclass
class GroupWritebackConfiguration(WritebackConfiguration):
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the target on-premises group type the cloud object is written back as. Nullable. The possible values are: universalDistributionGroup, universalSecurityGroup, universalMailEnabledSecurityGroup.If the cloud group is a unified (Microsoft 365) group, this property can be one of the following: universalDistributionGroup, universalSecurityGroup, universalMailEnabledSecurityGroup. Microsoft Entra security groups can be written back as universalSecurityGroup. If isEnabled or the NewUnifiedGroupWritebackDefault group setting is true but this property isn't explicitly configured: Microsoft 365 groups are written back as universalDistributionGroup by defaultSecurity groups are written back as universalSecurityGroup by default
    on_premises_group_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupWritebackConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupWritebackConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GroupWritebackConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .writeback_configuration import WritebackConfiguration

        from .writeback_configuration import WritebackConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "onPremisesGroupType": lambda n : setattr(self, 'on_premises_group_type', n.get_str_value()),
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
        writer.write_str_value("onPremisesGroupType", self.on_premises_group_type)
    

