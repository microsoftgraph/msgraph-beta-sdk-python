from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_callout_extension = lazy_import('msgraph.generated.models.custom_callout_extension')
custom_extension_callback_configuration = lazy_import('msgraph.generated.models.custom_extension_callback_configuration')
user = lazy_import('msgraph.generated.models.user')

class CustomTaskExtension(custom_callout_extension.CustomCalloutExtension):
    @property
    def callback_configuration(self,) -> Optional[custom_extension_callback_configuration.CustomExtensionCallbackConfiguration]:
        """
        Gets the callbackConfiguration property value. The callback configuration for a custom extension.
        Returns: Optional[custom_extension_callback_configuration.CustomExtensionCallbackConfiguration]
        """
        return self._callback_configuration
    
    @callback_configuration.setter
    def callback_configuration(self,value: Optional[custom_extension_callback_configuration.CustomExtensionCallbackConfiguration] = None) -> None:
        """
        Sets the callbackConfiguration property value. The callback configuration for a custom extension.
        Args:
            value: Value to set for the callbackConfiguration property.
        """
        self._callback_configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CustomTaskExtension and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.identityGovernance.customTaskExtension"
        # The callback configuration for a custom extension.
        self._callback_configuration: Optional[custom_extension_callback_configuration.CustomExtensionCallbackConfiguration] = None
        # The unique identifier of the Azure AD user that created the custom task extension.Supports $filter(eq, ne) and $expand.
        self._created_by: Optional[user.User] = None
        # When the custom task extension was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._created_date_time: Optional[datetime] = None
        # The unique identifier of the Azure AD user that modified the custom task extension last.Supports $filter(eq, ne) and $expand.
        self._last_modified_by: Optional[user.User] = None
        # When the custom extension was last modified.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        self._last_modified_date_time: Optional[datetime] = None
    
    @property
    def created_by(self,) -> Optional[user.User]:
        """
        Gets the createdBy property value. The unique identifier of the Azure AD user that created the custom task extension.Supports $filter(eq, ne) and $expand.
        Returns: Optional[user.User]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[user.User] = None) -> None:
        """
        Sets the createdBy property value. The unique identifier of the Azure AD user that created the custom task extension.Supports $filter(eq, ne) and $expand.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. When the custom task extension was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. When the custom task extension was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomTaskExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomTaskExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomTaskExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "callback_configuration": lambda n : setattr(self, 'callback_configuration', n.get_object_value(custom_extension_callback_configuration.CustomExtensionCallbackConfiguration)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(user.User)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(user.User)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_by(self,) -> Optional[user.User]:
        """
        Gets the lastModifiedBy property value. The unique identifier of the Azure AD user that modified the custom task extension last.Supports $filter(eq, ne) and $expand.
        Returns: Optional[user.User]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[user.User] = None) -> None:
        """
        Sets the lastModifiedBy property value. The unique identifier of the Azure AD user that modified the custom task extension last.Supports $filter(eq, ne) and $expand.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. When the custom extension was last modified.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. When the custom extension was last modified.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("callbackConfiguration", self.callback_configuration)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

