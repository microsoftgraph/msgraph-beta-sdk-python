from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PowerliftIncidentMetadata(AdditionalDataHolder, Parsable):
    """
    Collection of app diagnostics associated with a user.
    """
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
    def application(self,) -> Optional[str]:
        """
        Gets the application property value. The name of the application the diagnostic is from. Example: com.microsoft.CompanyPortal
        Returns: Optional[str]
        """
        return self._application
    
    @application.setter
    def application(self,value: Optional[str] = None) -> None:
        """
        Sets the application property value. The name of the application the diagnostic is from. Example: com.microsoft.CompanyPortal
        Args:
            value: Value to set for the application property.
        """
        self._application = value
    
    @property
    def client_version(self,) -> Optional[str]:
        """
        Gets the clientVersion property value. The version of the application. Example: 5.2203.1
        Returns: Optional[str]
        """
        return self._client_version
    
    @client_version.setter
    def client_version(self,value: Optional[str] = None) -> None:
        """
        Sets the clientVersion property value. The version of the application. Example: 5.2203.1
        Args:
            value: Value to set for the clientVersion property.
        """
        self._client_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new powerliftIncidentMetadata and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The name of the application the diagnostic is from. Example: com.microsoft.CompanyPortal
        self._application: Optional[str] = None
        # The version of the application. Example: 5.2203.1
        self._client_version: Optional[str] = None
        # The time the app diagnostic was created. Example: 2022-04-19T17:24:45.313Z
        self._created_at_date_time: Optional[datetime] = None
        # The unique app diagnostic identifier as a user friendly 8 character hexadecimal string. Example: 8520467A
        self._easy_id: Optional[str] = None
        # A list of files that are associated with the diagnostic.
        self._file_names: Optional[List[str]] = None
        # The locale information of the application. Example: en-US
        self._locale: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The device's OS the diagnostic is from. Example: iOS
        self._platform: Optional[str] = None
        # The unique identifier of the app diagnostic. Example: 8520467a-49a9-44a4-8447-8dfb8bec6726
        self._powerlift_id: Optional[Guid] = None
    
    @property
    def created_at_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdAtDateTime property value. The time the app diagnostic was created. Example: 2022-04-19T17:24:45.313Z
        Returns: Optional[datetime]
        """
        return self._created_at_date_time
    
    @created_at_date_time.setter
    def created_at_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdAtDateTime property value. The time the app diagnostic was created. Example: 2022-04-19T17:24:45.313Z
        Args:
            value: Value to set for the createdAtDateTime property.
        """
        self._created_at_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PowerliftIncidentMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PowerliftIncidentMetadata
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PowerliftIncidentMetadata()
    
    @property
    def easy_id(self,) -> Optional[str]:
        """
        Gets the easyId property value. The unique app diagnostic identifier as a user friendly 8 character hexadecimal string. Example: 8520467A
        Returns: Optional[str]
        """
        return self._easy_id
    
    @easy_id.setter
    def easy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the easyId property value. The unique app diagnostic identifier as a user friendly 8 character hexadecimal string. Example: 8520467A
        Args:
            value: Value to set for the easyId property.
        """
        self._easy_id = value
    
    @property
    def file_names(self,) -> Optional[List[str]]:
        """
        Gets the fileNames property value. A list of files that are associated with the diagnostic.
        Returns: Optional[List[str]]
        """
        return self._file_names
    
    @file_names.setter
    def file_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the fileNames property value. A list of files that are associated with the diagnostic.
        Args:
            value: Value to set for the fileNames property.
        """
        self._file_names = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application": lambda n : setattr(self, 'application', n.get_str_value()),
            "client_version": lambda n : setattr(self, 'client_version', n.get_str_value()),
            "created_at_date_time": lambda n : setattr(self, 'created_at_date_time', n.get_datetime_value()),
            "easy_id": lambda n : setattr(self, 'easy_id', n.get_str_value()),
            "file_names": lambda n : setattr(self, 'file_names', n.get_collection_of_primitive_values(str)),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "powerlift_id": lambda n : setattr(self, 'powerlift_id', n.get_object_value(Guid)),
        }
        return fields
    
    @property
    def locale(self,) -> Optional[str]:
        """
        Gets the locale property value. The locale information of the application. Example: en-US
        Returns: Optional[str]
        """
        return self._locale
    
    @locale.setter
    def locale(self,value: Optional[str] = None) -> None:
        """
        Sets the locale property value. The locale information of the application. Example: en-US
        Args:
            value: Value to set for the locale property.
        """
        self._locale = value
    
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
    
    @property
    def platform(self,) -> Optional[str]:
        """
        Gets the platform property value. The device's OS the diagnostic is from. Example: iOS
        Returns: Optional[str]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[str] = None) -> None:
        """
        Sets the platform property value. The device's OS the diagnostic is from. Example: iOS
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    @property
    def powerlift_id(self,) -> Optional[Guid]:
        """
        Gets the powerliftId property value. The unique identifier of the app diagnostic. Example: 8520467a-49a9-44a4-8447-8dfb8bec6726
        Returns: Optional[Guid]
        """
        return self._powerlift_id
    
    @powerlift_id.setter
    def powerlift_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the powerliftId property value. The unique identifier of the app diagnostic. Example: 8520467a-49a9-44a4-8447-8dfb8bec6726
        Args:
            value: Value to set for the powerliftId property.
        """
        self._powerlift_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("application", self.application)
        writer.write_str_value("clientVersion", self.client_version)
        writer.write_datetime_value("createdAtDateTime", self.created_at_date_time)
        writer.write_str_value("easyId", self.easy_id)
        writer.write_collection_of_primitive_values("fileNames", self.file_names)
        writer.write_str_value("locale", self.locale)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("platform", self.platform)
        writer.write_object_value("powerliftId", self.powerlift_id)
        writer.write_additional_data_value(self.additional_data)
    

