from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ApplicationSignInSummary(entity.Entity):
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. Name of the application that the user signed into.
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. Name of the application that the user signed into.
        Args:
            value: Value to set for the appDisplayName property.
        """
        self._app_display_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ApplicationSignInSummary and sets the default values.
        """
        super().__init__()
        # Name of the application that the user signed into.
        self._app_display_name: Optional[str] = None
        # Count of failed sign-ins made by the application.
        self._failed_sign_in_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Count of successful sign-ins made by the application.
        self._successful_sign_in_count: Optional[int] = None
        # Percentage of successful sign-ins made by the application.
        self._success_percentage: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplicationSignInSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationSignInSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApplicationSignInSummary()
    
    @property
    def failed_sign_in_count(self,) -> Optional[int]:
        """
        Gets the failedSignInCount property value. Count of failed sign-ins made by the application.
        Returns: Optional[int]
        """
        return self._failed_sign_in_count
    
    @failed_sign_in_count.setter
    def failed_sign_in_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedSignInCount property value. Count of failed sign-ins made by the application.
        Args:
            value: Value to set for the failedSignInCount property.
        """
        self._failed_sign_in_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_display_name": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "failed_sign_in_count": lambda n : setattr(self, 'failed_sign_in_count', n.get_int_value()),
            "successful_sign_in_count": lambda n : setattr(self, 'successful_sign_in_count', n.get_int_value()),
            "success_percentage": lambda n : setattr(self, 'success_percentage', n.get_float_value()),
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
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_int_value("failedSignInCount", self.failed_sign_in_count)
        writer.write_int_value("successfulSignInCount", self.successful_sign_in_count)
        writer.write_float_value("successPercentage", self.success_percentage)
    
    @property
    def successful_sign_in_count(self,) -> Optional[int]:
        """
        Gets the successfulSignInCount property value. Count of successful sign-ins made by the application.
        Returns: Optional[int]
        """
        return self._successful_sign_in_count
    
    @successful_sign_in_count.setter
    def successful_sign_in_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successfulSignInCount property value. Count of successful sign-ins made by the application.
        Args:
            value: Value to set for the successfulSignInCount property.
        """
        self._successful_sign_in_count = value
    
    @property
    def success_percentage(self,) -> Optional[float]:
        """
        Gets the successPercentage property value. Percentage of successful sign-ins made by the application.
        Returns: Optional[float]
        """
        return self._success_percentage
    
    @success_percentage.setter
    def success_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the successPercentage property value. Percentage of successful sign-ins made by the application.
        Args:
            value: Value to set for the successPercentage property.
        """
        self._success_percentage = value
    

