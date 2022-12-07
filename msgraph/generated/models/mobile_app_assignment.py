from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_and_app_management_assignment_source = lazy_import('msgraph.generated.models.device_and_app_management_assignment_source')
device_and_app_management_assignment_target = lazy_import('msgraph.generated.models.device_and_app_management_assignment_target')
entity = lazy_import('msgraph.generated.models.entity')
install_intent = lazy_import('msgraph.generated.models.install_intent')
mobile_app_assignment_settings = lazy_import('msgraph.generated.models.mobile_app_assignment_settings')

class MobileAppAssignment(entity.Entity):
    """
    A class containing the properties used for Group Assignment of a Mobile App.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new mobileAppAssignment and sets the default values.
        """
        super().__init__()
        # Possible values for the install intent chosen by the admin.
        self._intent: Optional[install_intent.InstallIntent] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The settings for target assignment defined by the admin.
        self._settings: Optional[mobile_app_assignment_settings.MobileAppAssignmentSettings] = None
        # Represents source of assignment.
        self._source: Optional[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource] = None
        # The identifier of the source of the assignment.
        self._source_id: Optional[str] = None
        # The target group assignment defined by the admin.
        self._target: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "intent": lambda n : setattr(self, 'intent', n.get_enum_value(install_intent.InstallIntent)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(mobile_app_assignment_settings.MobileAppAssignmentSettings)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource)),
            "source_id": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_object_value(device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def intent(self,) -> Optional[install_intent.InstallIntent]:
        """
        Gets the intent property value. Possible values for the install intent chosen by the admin.
        Returns: Optional[install_intent.InstallIntent]
        """
        return self._intent
    
    @intent.setter
    def intent(self,value: Optional[install_intent.InstallIntent] = None) -> None:
        """
        Sets the intent property value. Possible values for the install intent chosen by the admin.
        Args:
            value: Value to set for the intent property.
        """
        self._intent = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("intent", self.intent)
        writer.write_object_value("settings", self.settings)
        writer.write_enum_value("source", self.source)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_object_value("target", self.target)
    
    @property
    def settings(self,) -> Optional[mobile_app_assignment_settings.MobileAppAssignmentSettings]:
        """
        Gets the settings property value. The settings for target assignment defined by the admin.
        Returns: Optional[mobile_app_assignment_settings.MobileAppAssignmentSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[mobile_app_assignment_settings.MobileAppAssignmentSettings] = None) -> None:
        """
        Sets the settings property value. The settings for target assignment defined by the admin.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def source(self,) -> Optional[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource]:
        """
        Gets the source property value. Represents source of assignment.
        Returns: Optional[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource] = None) -> None:
        """
        Sets the source property value. Represents source of assignment.
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def source_id(self,) -> Optional[str]:
        """
        Gets the sourceId property value. The identifier of the source of the assignment.
        Returns: Optional[str]
        """
        return self._source_id
    
    @source_id.setter
    def source_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceId property value. The identifier of the source of the assignment.
        Args:
            value: Value to set for the sourceId property.
        """
        self._source_id = value
    
    @property
    def target(self,) -> Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget]:
        """
        Gets the target property value. The target group assignment defined by the admin.
        Returns: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None) -> None:
        """
        Sets the target property value. The target group assignment defined by the admin.
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

