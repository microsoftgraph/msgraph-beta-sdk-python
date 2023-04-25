from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import custom_callout_extension, custom_extension_callback_configuration

from . import custom_callout_extension

class AccessPackageAssignmentWorkflowExtension(custom_callout_extension.CustomCalloutExtension):
    def __init__(self,) -> None:
        """
        Instantiates a new AccessPackageAssignmentWorkflowExtension and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessPackageAssignmentWorkflowExtension"
        # The callback configuration for a custom extension.
        self._callback_configuration: Optional[custom_extension_callback_configuration.CustomExtensionCallbackConfiguration] = None
        # The userPrincipalName of the user or identity of the subject that created this resource. Read-only.
        self._created_by: Optional[str] = None
        # When the entity was created.
        self._created_date_time: Optional[datetime] = None
        # The userPrincipalName of the identity that last modified the entity.
        self._last_modified_by: Optional[str] = None
        # When the entity was last modified.
        self._last_modified_date_time: Optional[datetime] = None
    
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
            value: Value to set for the callback_configuration property.
        """
        self._callback_configuration = value
    
    @property
    def created_by(self,) -> Optional[str]:
        """
        Gets the createdBy property value. The userPrincipalName of the user or identity of the subject that created this resource. Read-only.
        Returns: Optional[str]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[str] = None) -> None:
        """
        Sets the createdBy property value. The userPrincipalName of the user or identity of the subject that created this resource. Read-only.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. When the entity was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. When the entity was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentWorkflowExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentWorkflowExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentWorkflowExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import custom_callout_extension, custom_extension_callback_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "callbackConfiguration": lambda n : setattr(self, 'callback_configuration', n.get_object_value(custom_extension_callback_configuration.CustomExtensionCallbackConfiguration)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_by(self,) -> Optional[str]:
        """
        Gets the lastModifiedBy property value. The userPrincipalName of the identity that last modified the entity.
        Returns: Optional[str]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[str] = None) -> None:
        """
        Sets the lastModifiedBy property value. The userPrincipalName of the identity that last modified the entity.
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. When the entity was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. When the entity was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
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
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

