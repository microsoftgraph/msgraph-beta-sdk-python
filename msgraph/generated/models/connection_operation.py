from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

connection_operation_status = lazy_import('msgraph.generated.models.connection_operation_status')
entity = lazy_import('msgraph.generated.models.entity')
public_error = lazy_import('msgraph.generated.models.public_error')

class ConnectionOperation(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ConnectionOperation and sets the default values.
        """
        super().__init__()
        # The error property
        self._error: Optional[public_error.PublicError] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[connection_operation_status.ConnectionOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConnectionOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConnectionOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConnectionOperation()
    
    @property
    def error(self,) -> Optional[public_error.PublicError]:
        """
        Gets the error property value. The error property
        Returns: Optional[public_error.PublicError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[public_error.PublicError] = None) -> None:
        """
        Sets the error property value. The error property
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(public_error.PublicError)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(connection_operation_status.ConnectionOperationStatus)),
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
        writer.write_object_value("error", self.error)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[connection_operation_status.ConnectionOperationStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[connection_operation_status.ConnectionOperationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[connection_operation_status.ConnectionOperationStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

