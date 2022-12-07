from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

setting = lazy_import('msgraph.generated.models.managed_tenants.setting')
workload_action_category = lazy_import('msgraph.generated.models.managed_tenants.workload_action_category')

class WorkloadAction(AdditionalDataHolder, Parsable):
    @property
    def action_id(self,) -> Optional[str]:
        """
        Gets the actionId property value. The unique identifier for the workload action. Required. Read-only.
        Returns: Optional[str]
        """
        return self._action_id
    
    @action_id.setter
    def action_id(self,value: Optional[str] = None) -> None:
        """
        Sets the actionId property value. The unique identifier for the workload action. Required. Read-only.
        Args:
            value: Value to set for the actionId property.
        """
        self._action_id = value
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def category(self,) -> Optional[workload_action_category.WorkloadActionCategory]:
        """
        Gets the category property value. The category for the workload action. Possible values are: automated, manual, unknownFutureValue. Optional. Read-only.
        Returns: Optional[workload_action_category.WorkloadActionCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[workload_action_category.WorkloadActionCategory] = None) -> None:
        """
        Sets the category property value. The category for the workload action. Possible values are: automated, manual, unknownFutureValue. Optional. Read-only.
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workloadAction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The unique identifier for the workload action. Required. Read-only.
        self._action_id: Optional[str] = None
        # The category for the workload action. Possible values are: automated, manual, unknownFutureValue. Optional. Read-only.
        self._category: Optional[workload_action_category.WorkloadActionCategory] = None
        # The description for the workload action. Optional. Read-only.
        self._description: Optional[str] = None
        # The display name for the workload action. Optional. Read-only.
        self._display_name: Optional[str] = None
        # The licenses property
        self._licenses: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The service associated with workload action. Optional. Read-only.
        self._service: Optional[str] = None
        # The collection of settings associated with the workload action. Optional. Read-only.
        self._settings: Optional[List[setting.Setting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkloadAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkloadAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkloadAction()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description for the workload action. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description for the workload action. Optional. Read-only.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the workload action. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the workload action. Optional. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_id": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(workload_action_category.WorkloadActionCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "licenses": lambda n : setattr(self, 'licenses', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(setting.Setting)),
        }
        return fields
    
    @property
    def licenses(self,) -> Optional[List[str]]:
        """
        Gets the licenses property value. The licenses property
        Returns: Optional[List[str]]
        """
        return self._licenses
    
    @licenses.setter
    def licenses(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the licenses property value. The licenses property
        Args:
            value: Value to set for the licenses property.
        """
        self._licenses = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("actionId", self.action_id)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("licenses", self.licenses)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("service", self.service)
        writer.write_collection_of_object_values("settings", self.settings)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service(self,) -> Optional[str]:
        """
        Gets the service property value. The service associated with workload action. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._service
    
    @service.setter
    def service(self,value: Optional[str] = None) -> None:
        """
        Sets the service property value. The service associated with workload action. Optional. Read-only.
        Args:
            value: Value to set for the service property.
        """
        self._service = value
    
    @property
    def settings(self,) -> Optional[List[setting.Setting]]:
        """
        Gets the settings property value. The collection of settings associated with the workload action. Optional. Read-only.
        Returns: Optional[List[setting.Setting]]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[List[setting.Setting]] = None) -> None:
        """
        Sets the settings property value. The collection of settings associated with the workload action. Optional. Read-only.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    

