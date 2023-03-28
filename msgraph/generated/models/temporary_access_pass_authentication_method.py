from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method

from . import authentication_method

class TemporaryAccessPassAuthenticationMethod(authentication_method.AuthenticationMethod):
    def __init__(self,) -> None:
        """
        Instantiates a new TemporaryAccessPassAuthenticationMethod and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.temporaryAccessPassAuthenticationMethod"
        # The date and time when the Temporary Access Pass was created.
        self._created_date_time: Optional[datetime] = None
        # Determines whether the pass is limited to a one-time use. If true, the pass can be used once; if false, the pass can be used multiple times within the Temporary Access Pass lifetime.
        self._is_usable_once: Optional[bool] = None
        # The lifetime of the Temporary Access Pass in minutes starting at startDateTime. Must be between 10 and 43200 inclusive (equivalent to 30 days).
        self._lifetime_in_minutes: Optional[int] = None
        # The date and time when the Temporary Access Pass becomes available to use and when isUsable is true is enforced.
        self._start_date_time: Optional[datetime] = None
        # The Temporary Access Pass used to authenticate. Returned only on creation of a new temporaryAccessPassAuthenticationMethod object; Hidden in subsequent read operations and returned as null with GET.
        self._temporary_access_pass: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the Temporary Access Pass was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the Temporary Access Pass was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TemporaryAccessPassAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TemporaryAccessPassAuthenticationMethod
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TemporaryAccessPassAuthenticationMethod()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isUsableOnce": lambda n : setattr(self, 'is_usable_once', n.get_bool_value()),
            "lifetimeInMinutes": lambda n : setattr(self, 'lifetime_in_minutes', n.get_int_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "temporaryAccessPass": lambda n : setattr(self, 'temporary_access_pass', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_usable_once(self,) -> Optional[bool]:
        """
        Gets the isUsableOnce property value. Determines whether the pass is limited to a one-time use. If true, the pass can be used once; if false, the pass can be used multiple times within the Temporary Access Pass lifetime.
        Returns: Optional[bool]
        """
        return self._is_usable_once
    
    @is_usable_once.setter
    def is_usable_once(self,value: Optional[bool] = None) -> None:
        """
        Sets the isUsableOnce property value. Determines whether the pass is limited to a one-time use. If true, the pass can be used once; if false, the pass can be used multiple times within the Temporary Access Pass lifetime.
        Args:
            value: Value to set for the is_usable_once property.
        """
        self._is_usable_once = value
    
    @property
    def lifetime_in_minutes(self,) -> Optional[int]:
        """
        Gets the lifetimeInMinutes property value. The lifetime of the Temporary Access Pass in minutes starting at startDateTime. Must be between 10 and 43200 inclusive (equivalent to 30 days).
        Returns: Optional[int]
        """
        return self._lifetime_in_minutes
    
    @lifetime_in_minutes.setter
    def lifetime_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the lifetimeInMinutes property value. The lifetime of the Temporary Access Pass in minutes starting at startDateTime. Must be between 10 and 43200 inclusive (equivalent to 30 days).
        Args:
            value: Value to set for the lifetime_in_minutes property.
        """
        self._lifetime_in_minutes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("isUsableOnce", self.is_usable_once)
        writer.write_int_value("lifetimeInMinutes", self.lifetime_in_minutes)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("temporaryAccessPass", self.temporary_access_pass)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The date and time when the Temporary Access Pass becomes available to use and when isUsable is true is enforced.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The date and time when the Temporary Access Pass becomes available to use and when isUsable is true is enforced.
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    
    @property
    def temporary_access_pass(self,) -> Optional[str]:
        """
        Gets the temporaryAccessPass property value. The Temporary Access Pass used to authenticate. Returned only on creation of a new temporaryAccessPassAuthenticationMethod object; Hidden in subsequent read operations and returned as null with GET.
        Returns: Optional[str]
        """
        return self._temporary_access_pass
    
    @temporary_access_pass.setter
    def temporary_access_pass(self,value: Optional[str] = None) -> None:
        """
        Sets the temporaryAccessPass property value. The Temporary Access Pass used to authenticate. Returned only on creation of a new temporaryAccessPassAuthenticationMethod object; Hidden in subsequent read operations and returned as null with GET.
        Args:
            value: Value to set for the temporary_access_pass property.
        """
        self._temporary_access_pass = value
    

