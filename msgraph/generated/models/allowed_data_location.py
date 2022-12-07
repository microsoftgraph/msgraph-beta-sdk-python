from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class AllowedDataLocation(entity.Entity):
    """
    Provides operations to manage the collection of allowedDataLocation entities.
    """
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The appId property
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The appId property
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new allowedDataLocation and sets the default values.
        """
        super().__init__()
        # The appId property
        self._app_id: Optional[str] = None
        # The domain property
        self._domain: Optional[str] = None
        # The isDefault property
        self._is_default: Optional[bool] = None
        # The location property
        self._location: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AllowedDataLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AllowedDataLocation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AllowedDataLocation()
    
    @property
    def domain(self,) -> Optional[str]:
        """
        Gets the domain property value. The domain property
        Returns: Optional[str]
        """
        return self._domain
    
    @domain.setter
    def domain(self,value: Optional[str] = None) -> None:
        """
        Sets the domain property value. The domain property
        Args:
            value: Value to set for the domain property.
        """
        self._domain = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. The isDefault property
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. The isDefault property
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def location(self,) -> Optional[str]:
        """
        Gets the location property value. The location property
        Returns: Optional[str]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[str] = None) -> None:
        """
        Sets the location property value. The location property
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("domain", self.domain)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_str_value("location", self.location)
    

