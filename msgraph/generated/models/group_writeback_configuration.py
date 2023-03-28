from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import writeback_configuration

from . import writeback_configuration

class GroupWritebackConfiguration(writeback_configuration.WritebackConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new GroupWritebackConfiguration and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates the target on-premise group type the cloud object will be written back as. Nullable. The possible values are: universalDistributionGroup, universalSecurityGroup, universalMailEnabledSecurityGroup.If the cloud group is a unified (Microsoft 365) group, this property can be one of the following: universalDistributionGroup, universalSecurityGroup, universalMailEnabledSecurityGroup. Azure AD security groups can be written back as universalSecurityGroup. If isEnabled or the NewUnifiedGroupWritebackDefault group setting is true but this property is not explicitly configured: Microsoft 365 groups will be written back as universalDistributionGroup by defaultSecurity groups will be written back as universalSecurityGroup by default
        self._on_premises_group_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupWritebackConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupWritebackConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupWritebackConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import writeback_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "onPremisesGroupType": lambda n : setattr(self, 'on_premises_group_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def on_premises_group_type(self,) -> Optional[str]:
        """
        Gets the onPremisesGroupType property value. Indicates the target on-premise group type the cloud object will be written back as. Nullable. The possible values are: universalDistributionGroup, universalSecurityGroup, universalMailEnabledSecurityGroup.If the cloud group is a unified (Microsoft 365) group, this property can be one of the following: universalDistributionGroup, universalSecurityGroup, universalMailEnabledSecurityGroup. Azure AD security groups can be written back as universalSecurityGroup. If isEnabled or the NewUnifiedGroupWritebackDefault group setting is true but this property is not explicitly configured: Microsoft 365 groups will be written back as universalDistributionGroup by defaultSecurity groups will be written back as universalSecurityGroup by default
        Returns: Optional[str]
        """
        return self._on_premises_group_type
    
    @on_premises_group_type.setter
    def on_premises_group_type(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesGroupType property value. Indicates the target on-premise group type the cloud object will be written back as. Nullable. The possible values are: universalDistributionGroup, universalSecurityGroup, universalMailEnabledSecurityGroup.If the cloud group is a unified (Microsoft 365) group, this property can be one of the following: universalDistributionGroup, universalSecurityGroup, universalMailEnabledSecurityGroup. Azure AD security groups can be written back as universalSecurityGroup. If isEnabled or the NewUnifiedGroupWritebackDefault group setting is true but this property is not explicitly configured: Microsoft 365 groups will be written back as universalDistributionGroup by defaultSecurity groups will be written back as universalSecurityGroup by default
        Args:
            value: Value to set for the on_premises_group_type property.
        """
        self._on_premises_group_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("onPremisesGroupType", self.on_premises_group_type)
    

