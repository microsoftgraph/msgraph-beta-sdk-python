from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
setup_status = lazy_import('msgraph.generated.models.setup_status')

class PrivilegedSignupStatus(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new PrivilegedSignupStatus and sets the default values.
        """
        super().__init__()
        # The isRegistered property
        self._is_registered: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[setup_status.SetupStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedSignupStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedSignupStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedSignupStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_registered": lambda n : setattr(self, 'is_registered', n.get_bool_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(setup_status.SetupStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_registered(self,) -> Optional[bool]:
        """
        Gets the isRegistered property value. The isRegistered property
        Returns: Optional[bool]
        """
        return self._is_registered
    
    @is_registered.setter
    def is_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRegistered property value. The isRegistered property
        Args:
            value: Value to set for the isRegistered property.
        """
        self._is_registered = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isRegistered", self.is_registered)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[setup_status.SetupStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[setup_status.SetupStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[setup_status.SetupStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

