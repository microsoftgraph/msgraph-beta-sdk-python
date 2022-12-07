from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_source_filter = lazy_import('msgraph.generated.models.authentication_source_filter')
entity = lazy_import('msgraph.generated.models.entity')

class AuthenticationListener(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationListener and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The priority of the listener. Determines the order of evaluation when an event has multiple listeners. The priority is evaluated from low to high.
        self._priority: Optional[int] = None
        # Filter based on the source of the authentication that is used to determine whether the listener is evaluated. This is currently limited to evaluations based on application the user is authenticating to.
        self._source_filter: Optional[authentication_source_filter.AuthenticationSourceFilter] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationListener
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationListener()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "source_filter": lambda n : setattr(self, 'source_filter', n.get_object_value(authentication_source_filter.AuthenticationSourceFilter)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. The priority of the listener. Determines the order of evaluation when an event has multiple listeners. The priority is evaluated from low to high.
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. The priority of the listener. Determines the order of evaluation when an event has multiple listeners. The priority is evaluated from low to high.
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("sourceFilter", self.source_filter)
    
    @property
    def source_filter(self,) -> Optional[authentication_source_filter.AuthenticationSourceFilter]:
        """
        Gets the sourceFilter property value. Filter based on the source of the authentication that is used to determine whether the listener is evaluated. This is currently limited to evaluations based on application the user is authenticating to.
        Returns: Optional[authentication_source_filter.AuthenticationSourceFilter]
        """
        return self._source_filter
    
    @source_filter.setter
    def source_filter(self,value: Optional[authentication_source_filter.AuthenticationSourceFilter] = None) -> None:
        """
        Sets the sourceFilter property value. Filter based on the source of the authentication that is used to determine whether the listener is evaluated. This is currently limited to evaluations based on application the user is authenticating to.
        Args:
            value: Value to set for the sourceFilter property.
        """
        self._source_filter = value
    

