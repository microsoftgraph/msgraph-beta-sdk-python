from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_listener = lazy_import('msgraph.generated.models.authentication_listener')
b2x_identity_user_flow = lazy_import('msgraph.generated.models.b2x_identity_user_flow')

class InvokeUserFlowListener(authentication_listener.AuthenticationListener):
    def __init__(self,) -> None:
        """
        Instantiates a new InvokeUserFlowListener and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.invokeUserFlowListener"
        # The user flow that is invoked when this action executes.
        self._user_flow: Optional[b2x_identity_user_flow.B2xIdentityUserFlow] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InvokeUserFlowListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InvokeUserFlowListener
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InvokeUserFlowListener()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "user_flow": lambda n : setattr(self, 'user_flow', n.get_object_value(b2x_identity_user_flow.B2xIdentityUserFlow)),
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
        writer.write_object_value("userFlow", self.user_flow)
    
    @property
    def user_flow(self,) -> Optional[b2x_identity_user_flow.B2xIdentityUserFlow]:
        """
        Gets the userFlow property value. The user flow that is invoked when this action executes.
        Returns: Optional[b2x_identity_user_flow.B2xIdentityUserFlow]
        """
        return self._user_flow
    
    @user_flow.setter
    def user_flow(self,value: Optional[b2x_identity_user_flow.B2xIdentityUserFlow] = None) -> None:
        """
        Sets the userFlow property value. The user flow that is invoked when this action executes.
        Args:
            value: Value to set for the userFlow property.
        """
        self._user_flow = value
    

