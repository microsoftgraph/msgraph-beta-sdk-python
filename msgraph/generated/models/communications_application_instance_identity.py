from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')

class CommunicationsApplicationInstanceIdentity(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new CommunicationsApplicationInstanceIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.communicationsApplicationInstanceIdentity"
        # True if the participant would not like to be shown in other participants' rosters.
        self._hidden: Optional[bool] = None
        # The application's tenant ID.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CommunicationsApplicationInstanceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CommunicationsApplicationInstanceIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CommunicationsApplicationInstanceIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hidden(self,) -> Optional[bool]:
        """
        Gets the hidden property value. True if the participant would not like to be shown in other participants' rosters.
        Returns: Optional[bool]
        """
        return self._hidden
    
    @hidden.setter
    def hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the hidden property value. True if the participant would not like to be shown in other participants' rosters.
        Args:
            value: Value to set for the hidden property.
        """
        self._hidden = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The application's tenant ID.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The application's tenant ID.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

